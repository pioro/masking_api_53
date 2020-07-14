# masking_api_53
Masking Python SDK API generated via Swagger Client

Use the following command to regernate files - replace x.x.x.x with engine name or IP

 docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli generate -DapiDocs=false -DapiTests=false -DmodelTests=false -DmodelDocs=false -i http://x.x.x.x/masking/api/swagger-basepath.json -l python -o /local/ -DpackageName=masking_api_53

