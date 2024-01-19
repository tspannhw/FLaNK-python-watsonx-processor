# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import re
from nifiapi.flowfiletransform import FlowFileTransform, FlowFileTransformResult
from nifiapi.properties import PropertyDescriptor, StandardValidators, ExpressionLanguageScope

# https://github.com/IBM/watsonxdata-python-sdk
# pip install ibm-watsonxdata

class CallWatsonXAI(FlowFileTransform):
    class Java:
        implements = ['org.apache.nifi.python.processor.FlowFileTransform']

    class ProcessorDetails:
        version = '2.0.0-SNAPSHOT'
        description = """Output results of call to WatsonX.AI """
        tags = ["ibm", "WatsonX", "WatsonXAI", "generativeai", "ai", "artificial intelligence", "ml", "machine learning", "text", "LLM"]

    PROMPT_TEXT = PropertyDescriptor(
        name="Prompt Text",
        description="Specifies whether or not the text (including full prompt with context) to send",
        required=True,
        validators=[StandardValidators.NON_EMPTY_VALIDATOR],
        expression_language_scope=ExpressionLanguageScope.FLOWFILE_ATTRIBUTES
    )
    WATSONXAI_API_KEY = PropertyDescriptor(
        name="WatsonX AI API Key",
        description="The API Key to use in order to authentication with IBM WatsonX",
        sensitive=True,
        required=True,
        validators=[StandardValidators.NON_EMPTY_VALIDATOR],
        expression_language_scope=ExpressionLanguageScope.FLOWFILE_ATTRIBUTES
    )
    WATSONXAI_PROJECT_ID = PropertyDescriptor(
        name="WatsonX AI Project ID",
        description="The Project ID for WatsonX",
        sensitive=True,
        required=True,
        validators=[StandardValidators.NON_EMPTY_VALIDATOR],
        expression_language_scope=ExpressionLanguageScope.FLOWFILE_ATTRIBUTES
    )

    property_descriptors = [
        PROMPT_TEXT,
        WATSONXAI_API_KEY,
        WATSONXAI_PROJECT_ID
    ]

    def __init__(self, **kwargs):
        super().__init__()
        self.property_descriptors.append(self.PROMPT_TEXT)
        self.property_descriptors.append(self.WATSONXAI_API_KEY)
        self.property_descriptors.append(self.WATSONXAI_PROJECT_ID)

    def getPropertyDescriptors(self):
        return self.property_descriptors

    def transform(self, context, flowfile):
        from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes
        from ibm_watson_machine_learning.foundation_models import Model

        prompt_text = context.getProperty(self.PROMPT_TEXT).evaluateAttributeExpressions(flowfile).getValue()
        watsonx_api_key = context.getProperty(self.WATSONXAI_API_KEY).evaluateAttributeExpressions(flowfile).getValue()
        project_id = context.getProperty(self.WATSONXAI_PROJECT_ID).evaluateAttributeExpressions(flowfile).getValue()

        my_credentials = { 
            "url"    : "https://us-south.ml.cloud.ibm.com", 
            "apikey" : watsonx_api_key
        }

        model_id    = ModelTypes.LLAMA_2_70B_CHAT
        gen_parms   = None
        project_id  = project_id
        space_id    = None
        verify      = False

        model = Model( model_id, my_credentials, gen_parms, project_id, space_id, verify )
        gen_parms_override = None
        generated_response = model.generate( prompt_text, gen_parms_override )

        attributes = {"mime.type": "application/json"}
        output_contents = json.dumps(generated_response)

        self.logger.debug(f"Prompt: {prompt_text}")

        return FlowFileTransformResult(relationship = "success", contents=output_contents, attributes=attributes)
