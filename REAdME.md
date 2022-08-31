# Introduction: URL Shortner Design
the goal that we want to accomplish is to take a look at a system design for `URL Shortener` and implement its main features [ `shortening, redirecting` ]. It is important that we gather and ask questions in order to understand our domain and what limitations we have. Also, it is important to understand how the system should behave which will be explained in the bullet point list.

# Archeticture and Explanation

## How the System should behave (Main Features)

- `POST` request will take `long_url` and turn it into `short_url` which is a combination of `(0,9)` and characters `(a-z, A-Z)`
- `GET` will be responsible to handle `GET "/<short_url>"` requests. Which means users will paste `short_url` and then we fetch it from our DB to get `long_url` for that corresponding `short_url` and after that we redirect them to `long_url`

## How the System will Accomplish its Goals:

  . There are multiple ways to achieve this behavior in this repo I have used a `base62` converter and `global_unique_key_generator`. So, first I start by generating `global_unique_key` with. However, generating a `global_unique_key` is a problem by itself and this is not the scope of this repo. Therefore, I looked into existing solutions [short uuid](https://pypi.org/project/shortuuid/). The second step is to hash this value and convert to `base 62` which includes [0-9, a….z, A…Z] therefore its name is `base_62`. The pieces to solve this problem is gathered all, what we need to do now is to glue them. In our DB , in this case `SQLite`, we will have 3 columns. One to store `global_unique_key`. The other one will be to store the hash we will call it `short_url` and the last one is `long_url`. 
