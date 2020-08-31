vcl 4.0;

import std;

backend default {
  .host = "loadbalancer";
  .port = "5000";
  .first_byte_timeout = 600s;
}
