# frumpy

A *frumpy* API is a subset of the APIs that can described using Swagger.

`POST /pets:addPet`

* Only application/json
* Ignore unknown fields
* Status codes
  * 200 OK
  * 400 Bad Request
  * 401 Unauthorized
  * 403 Forbidden
  * 500 Internal Server Error
  * 503 Service Unavailable
* Only POST allowed
* Reponses are "one of", kind of like responses in gRPC

## Why not "REST"?
It depends what you mean with REST.

If you mean "stateless operations on resources" then you can achieve that in a frumpy way.

If you mean "limiting your operations to HTTP Verbs" then you should read the next section.

## Why only POST?
HTTP Verbs where designed primarily for managing text documents. If that is not what your API is doing there is a very good chance that the verbs do not match.

Have you ever spent half a day trying to figure out the "correct" way of, for example, activating a user?
Now ask yourself how the solution you came up with is better than `POST /users:activate`.
Was you answer "My solution is more RESTful"? If not, please let me know.

## Work in progress
https://petstore.swagger.io/?url=https://raw.githubusercontent.com/vandmo/frumpy/master/petstore.yaml
