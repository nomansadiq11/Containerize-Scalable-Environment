vcl 4.0;

import std;

backend default {
  .host = "webserver1";
  .port = "80";
  .first_byte_timeout = 600s;
}
