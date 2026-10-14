import http from "k6/http";
import { check, sleep } from "k6";

export const options = {
  scenarios: {
    carga: {
      executor: "constant-vus",
      vus: Number(__ENV.VUS ?? 5),
      duration: "2m",
    },
  },
};

export default function () {
  const res = http.get("http://localhost:8080/cafes");

  check(res, {
    "status HTTP 200": (r) => r.status === 200,
  });

  sleep(0.1);
}
