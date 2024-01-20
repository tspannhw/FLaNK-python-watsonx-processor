from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes
from ibm_watson_machine_learning.foundation_models import Model
import json

my_credentials = { 
    "url"    : "https://us-south.ml.cloud.ibm.com", 
    "apikey" : "myapikeyisprettyeasygetyourown"
}

model_id    = ModelTypes.LLAMA_2_70B_CHAT
gen_parms   = None
project_id  = "createaprojectinpromptlabandgrabtheidlistedinthetestcurl"
space_id    = None
verify      = False

model = Model( model_id, my_credentials, gen_parms, project_id, space_id, verify )

model_details = model.get_details()

print( json.dumps( model_details, indent=2 ) )
print (" " )
context_txt = "Apache NiFi 1.22 Updates Apache NiFi 1.22 Updates Apache NiFi 1.22 is now available for download! NASA on Unsplash Apache NiFi Downloads Apache NiFi Project Keys can be used to verify downloads. Please allow up to 24 hours for mirrors to synchronize…nifi.apache.org I recommend you add some extra NARs for your NiFi deployment. GitHub - tspannhw/FLaNK-NARs: NARs NARs. Contribute to tspannhw/FLaNK-NARs development by creating an account on GitHub.github.com The NiFi Media NAR is a great one and includes my processor based on Tika for parsing PDFs and Documents. A List of new features, updates and fixes: MiNiFi/C2 - Support access via LB / Proxy While the Heartbeat and Acknowledge communication from the agents can be configured via reverse proxy / load balancer…issues.apache.org Expose JMX metrics from NiFi JVM Most of the NiFi processors use external libraries which may register JMX Beans like Kafka processors. Exposing such…issues.apache.org Add a ModifyCompression processor If a user would like to convert from one compression format to another, they currently have to use CompressContent to…issues.apache.org Add Azure Queue Storage Processors using Azure SDK 12 The GetAzureQueueStorage and PutAzureQueueStorage Processors depend on the legacy Microsoft Azure SDK libraries. The…issues.apache.org Add ADLSCredentialsControllerServiceLookup Edit descriptionissues.apache.org Add AzureStorageCredentialsControllerServiceLookup_v12 Similar to AzureStorageCredentialsControllerServiceLookup, add a lookup service for the v12 blob processors…issues.apache.org AttributeToJSON: Nested JSON The AttributesToJSON processor does not Support NestedJSON. NestedJSON is supported both in content and in attributes…issues.apache.org Upgrade Apache Tika to 2.7.0 Edit descriptionissues.apache.org Image Viewer not available in Apache NiFi release The image viewer in the UI (used to display JPEG, GIF, WEBP, etc.) is in the nifi-media-nar, which is no longer…issues.apache.org Deprecate ECMAScript Script Engine Edit descriptionissues.apache.org Deprecate Lua and Ruby Script Engines The lua and ruby Script Engines for multiple scripted Processors and Controller Services should be deprecated for…issues.apache.org Release Date: June 11, 2023 A full list of issues that were resolved can be found at: Release Notes - ASF JIRA Release Notes - Apache NiFi - Version 1.22.0 - HTML formatissues.apache.org Deprecated Components and Features Apache NiFi supports a large number of extension components for integrating with a variety of products and services…cwiki.apache.org NiFi CLI Update to export and import all! Add Export/Import All - NiFi CLI - NiFi Registry In NiFi Toolkit, in the CLI, we currently have the following commands available: registry list-buckets registry…issues.apache.org https://www.apache.org/dyn/closer.lua?path=/nifi/1.22.0/nifi-toolkit-1.22.0-bin.zip registry import-all-flows That’s a lot of reason to upgrade, if you are on NiFi 1.20 or earlier it’s a no brainer. Even if you are on NiFi 1.21, they bug fixes alone are worth it. This should be it for a few months, but additional releases may come fast as the sprint towards NiFi 2.0 continues. https://attend.cloudera.com/nificommitters0503 Data In Motion apache nifi,data in motion,cloudera,hortonworks,minifi,kafka,spark streaming,schema registry,nifi…www.datainmotion.dev Apache NiFi 1.21/1.20 Updates Create processor for triggering HMS events Create a processor which is capable to trigger HiveMetaStore actions and generate notifications for them. The main goal…issues.apache.org Add Put Processor for Apache IoTDB Hi, folks I'm a contributer of Apache IoTDB. Recently, I have implemented a processor which can write data to IoTDB…issues.apache.org Add GenerateRecord processor to populate records with random data Similar to , this Jira proposes a GenerateRecord processor to generate dummy data into outgoing FlowFiles. There was a…issues.apache.org"

prompt_txt = "\n\n\nInput: How do I store to Apache Iceberg with Apache NiFi?"
gen_parms_override = None

generated_response = model.generate( context_txt + prompt_txt, gen_parms_override )

print( json.dumps( generated_response, indent=2 ) )
