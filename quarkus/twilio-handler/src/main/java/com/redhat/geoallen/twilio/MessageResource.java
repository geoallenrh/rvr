package com.redhat.geoallen.twilio;

import com.redhat.geoallen.twilio.beans.TwilioMessage;
import java.lang.String;
import javax.ws.rs.Consumes;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;

import java.util.HashMap;
import java.util.Map;

import io.reactivex.Flowable;
import org.eclipse.microprofile.reactive.streams.operators.PublisherBuilder;
import org.eclipse.microprofile.reactive.streams.operators.ReactiveStreams;

import org.eclipse.microprofile.reactive.messaging.Message;
import org.eclipse.microprofile.reactive.messaging.Outgoing;
import io.smallrye.reactive.messaging.kafka.KafkaMessage;
import kafka.utils.json.JsonObject;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.ser.std.ObjectArraySerializer;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import io.vertx.core.Vertx;
import io.vertx.kafka.client.producer.KafkaProducer;
import io.vertx.kafka.client.producer.KafkaProducerRecord;


import org.eclipse.microprofile.config.inject.ConfigProperty;
import javax.inject.Inject;
import org.jboss.resteasy.annotations.*;
import javax.annotation.PostConstruct;

import javax.enterprise.context.ApplicationScoped;

/**
 * A JAX-RS interface.  An implementation of this interface must be provided.
 */
@Path("/message")
//@ApplicationScoped
public class MessageResource {

  @Inject
    Vertx vertx;

  @Inject
    ObjectMapper objectMapper;

  @ConfigProperty(name = "kafka.bootstrap.servers")
    String kafkaBootstrapServer;

    private KafkaProducer<String, String> producer;


  @PostConstruct
    void initKafkaClient() {
        Map<String, String> config = new HashMap<>();
        config.put("bootstrap.servers", kafkaBootstrapServer);
        config.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        config.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        System.out.println("bootstrapping Kafka with config: " + config);

        producer = KafkaProducer.create(vertx, config);
    }


  

  @POST
  @Produces("text/xml")
  @Consumes("application/x-www-form-urlencoded")
  public String post(@Form TwilioMessage body) {
    System.out.println("Twilio Message Received");
    System.out.println(body.getAccountSid());
    sendMessageToKafka(body);
    String response = "<Response><Message>We got your message, thank you!</Message></Response>";
    return response;
  }

  


    public void sendMessageToKafka(TwilioMessage twilioMessage) {
      
      try {
         String jsonMessage = objectMapper.writeValueAsString(twilioMessage);
         String jsonKey = objectMapper.writeValueAsString(twilioMessage.getMessageSid());
         System.out.println("Message:" + jsonMessage);
         System.out.println("Key: " + jsonKey);
          KafkaProducerRecord<String, String> record = KafkaProducerRecord.create("twilio-in",jsonKey, jsonMessage);
          producer.write(record, done -> System.out.println("Kafka message sent: twilio message - " + twilioMessage.getBody()));
      } catch (Exception e) {
          e.printStackTrace();
      }
  }
  
}
