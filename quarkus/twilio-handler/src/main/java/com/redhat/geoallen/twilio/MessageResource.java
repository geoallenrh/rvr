package com.redhat.geoallen.twilio;

import com.redhat.geoallen.twilio.beans.TwilioMessage;
import java.lang.String;
import java.util.HashMap;
import java.util.Map;

import javax.ws.rs.Consumes;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;

import javax.inject.Inject;

import javax.annotation.PostConstruct;

import com.fasterxml.jackson.databind.ObjectMapper;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import io.vertx.core.Vertx;
import io.vertx.kafka.client.producer.KafkaProducer;
import io.vertx.kafka.client.producer.KafkaProducerRecord;

import org.eclipse.microprofile.config.inject.ConfigProperty;

import org.jboss.resteasy.annotations.*;


/**
 * JAX-RS implementation that accepts the Twilio url/encoded resquest, bind  to TwilioMessage POJO and then send to Kafka topic as JSON.
 */
@Path("/message")

public class MessageResource {

  @Inject
    Vertx vertx;

  @Inject
    ObjectMapper objectMapper;

  @ConfigProperty(name = "kafka.bootstrap.servers")
    String kafkaBootstrapServer;

  @ConfigProperty(name = "kafka.twilio.topic")
    String twilio_in_topic;

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
    String response = "<Response><Message>Thank You!  We received your message: '" + body.getBody() +"' </Message></Response>";
    return response;
  }


    public void sendMessageToKafka(TwilioMessage twilioMessage) {
      
      try {
         String jsonMessage = objectMapper.writeValueAsString(twilioMessage);
         String jsonKey = objectMapper.writeValueAsString(twilioMessage.getMessageSid());
         System.out.println("Message:" + jsonMessage);
         System.out.println("Key: " + jsonKey);
          KafkaProducerRecord<String, String> record = KafkaProducerRecord.create(twilio_in_topic,jsonKey, jsonMessage);
          producer.write(record, done -> System.out.println("Kafka message sent: twilio message - " + twilioMessage.getBody()));
      } catch (Exception e) {
          e.printStackTrace();
      }
  }
  
}
