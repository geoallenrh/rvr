
package com.redhat.geoallen.twilio.beans;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import javax.ws.rs.FormParam;



/**
 * Incoming SMS message from Twilio
 * 
 */

public class TwilioMessage {

    /**
     * 
     */
    @FormParam("ApiVersion")
    private String apiVersion;
    /**
     * 
     * (Required)
     * 
     */
    @FormParam("SmsSid")
    private String smsSid;
    @FormParam("SmsMessageSid")
    private String smsMessageSid;
    @FormParam("NumSegments")
    private String numSegments;
    @FormParam("From")
    private String from;
    @FormParam("ToState")
    private String toState;
    @FormParam("MessageSid")
    private String messageSid;
    @FormParam("AccountSid")
    private String accountSid;
    @FormParam("ToZip")
    private String toZip;
    @FormParam("FromCountry")
    private String fromCountry;
    @FormParam("ToCity")
    private String toCity;
    @FormParam("FromCity")
    private String fromCity;
    @FormParam("To")
    private String to;
    @FormParam("FromZip")
    private String fromZip;
    @FormParam("Body")
    private String body;
    @FormParam("ToCountry")
    private String toCountry;
    @FormParam("FromState")
    private String fromState;
    @FormParam("NumMedia")
    private String numMedia;

    /**
     * 
     */
    @FormParam("ApiVersion")
    public String getApiVersion() {
        return apiVersion;
    }

    /**
     * 
     */
    @FormParam("ApiVersion")
    public void setApiVersion(String apiVersion) {
        this.apiVersion = apiVersion;
    }

    /**
     * 
     * (Required)
     * 
     */
    @FormParam("SmsSid")
    public String getSmsSid() {
        return smsSid;
    }

    /**
     * 
     * (Required)
     * 
     */
    @FormParam("SmsSid")
    public void setSmsSid(String smsSid) {
        this.smsSid = smsSid;
    }

    @FormParam("SmsMessageSid")
    public String getSmsMessageSid() {
        return smsMessageSid;
    }

    @FormParam("SmsMessageSid")
    public void setSmsMessageSid(String smsMessageSid) {
        this.smsMessageSid = smsMessageSid;
    }

    @FormParam("NumSegments")
    public String getNumSegments() {
        return numSegments;
    }

    @FormParam("NumSegments")
    public void setNumSegments(String numSegments) {
        this.numSegments = numSegments;
    }

    @FormParam("From")
    public String getFrom() {
        return from;
    }

    @FormParam("From")
    public void setFrom(String from) {
        this.from = from;
    }

    @FormParam("ToState")
    public String getToState() {
        return toState;
    }

    @FormParam("ToState")
    public void setToState(String toState) {
        this.toState = toState;
    }

    @FormParam("MessageSid")
    public String getMessageSid() {
        return messageSid;
    }

    @FormParam("MessageSid")
    public void setMessageSid(String messageSid) {
        this.messageSid = messageSid;
    }

    @FormParam("AccountSid")
    public String getAccountSid() {
        return accountSid;
    }

    @FormParam("AccountSid")
    public void setAccountSid(String accountSid) {
        this.accountSid = accountSid;
    }

    @FormParam("ToZip")
    public String getToZip() {
        return toZip;
    }

    @FormParam("ToZip")
    public void setToZip(String toZip) {
        this.toZip = toZip;
    }

    @FormParam("FromCountry")
    public String getFromCountry() {
        return fromCountry;
    }

    @FormParam("FromCountry")
    public void setFromCountry(String fromCountry) {
        this.fromCountry = fromCountry;
    }

    @FormParam("ToCity")
    public String getToCity() {
        return toCity;
    }

    @FormParam("ToCity")
    public void setToCity(String toCity) {
        this.toCity = toCity;
    }

    @FormParam("FromCity")
    public String getFromCity() {
        return fromCity;
    }

    @FormParam("FromCity")
    public void setFromCity(String fromCity) {
        this.fromCity = fromCity;
    }

    @FormParam("To")
    public String getTo() {
        return to;
    }

    @FormParam("To")
    public void setTo(String to) {
        this.to = to;
    }

    @FormParam("FromZip")
    public String getFromZip() {
        return fromZip;
    }

    @FormParam("FromZip")
    public void setFromZip(String fromZip) {
        this.fromZip = fromZip;
    }

    @FormParam("Body")
    public String getBody() {
        return body;
    }

    @FormParam("Body")
    public void setBody(String body) {
        this.body = body;
    }

    @FormParam("ToCountry")
    public String getToCountry() {
        return toCountry;
    }

    @FormParam("ToCountry")
    public void setToCountry(String toCountry) {
        this.toCountry = toCountry;
    }

    @FormParam("FromState")
    public String getFromState() {
        return fromState;
    }

    @FormParam("FromState")
    public void setFromState(String fromState) {
        this.fromState = fromState;
    }

    @FormParam("NumMedia")
    public String getNumMedia() {
        return numMedia;
    }

    @FormParam("NumMedia")
    public void setNumMedia(String numMedia) {
        this.numMedia = numMedia;
    }

}
