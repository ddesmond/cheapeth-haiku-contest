import json
import requests
from datetime import datetime

class ctHiku:
    def __init__(self):
        self.line1_str = ""
        self.line2_str = ""
        self.line3_str = ""
        self.line4_str = ""

    def set_line1(self, lb_datetime):
        month_name = lb_datetime.strftime("%B")
        l_tmpl = f"The month was {month_name}"
        self.line1_str = l_tmpl

    def set_line2(self, lb_datetime):
        elem1 = ""
        elem2 = ""
        if lb_datetime.hour <= 12:
            elem1 = "day"
            elem2 = "gay"
        else:
            elem1 = "night"
            elem2 = "tight"
        l_tmpl = f"And the {elem1} was {elem2}"
        self.line2_str = l_tmpl

    def set_line3(self, lb_number):
        l_tmpl = f"When block number {lb_number}"
        self.line3_str = l_tmpl

    def set_line4(self, lb_datetime):
        elem1 = ""
        if lb_datetime.hour <= 12:
            elem1 = "pushed to array"
        else:
            elem1 = "lost in flight"
        l_tmpl = f"Was {elem1}"
        self.line4_str = l_tmpl

    def print_hiku(self):
        print()
        print(self.line1_str)
        print(self.line2_str)
        print(self.line3_str)
        print(self.line4_str)
        print()




def rpc_request_to_json(payload):
    url = "https://node.cheapeth.org/rpc"
    headers = {"content-type": "application/json"}

    # Example echo method
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.json()


def main():

    # get latest block
    lb_payload = {
        "method": "eth_blockNumber",
        "id": 0
    }
    lb_resp = rpc_request_to_json(lb_payload)
    lb_num_raw = lb_resp["result"]
    lb_num_b10 = int(lb_num_raw, 16)

    print(f"Latest Block Found: #{lb_num_b10}")


    payload2 = {
        "method": "eth_getBlockByNumber",
        "params": [lb_num_raw, False],
        "id": 0

    }
    response2 = rpc_request_to_json(payload2)
    
    lb_res2 = response2["result"]
    lb_timestamp_raw =  lb_res2["timestamp"]

    lb_ts = int(lb_timestamp_raw, 16)
    lb_dt = datetime.utcfromtimestamp(lb_ts)
    
    lb_dt_str = lb_dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"Timestamp: {lb_dt_str}")


    hiku = ctHiku()
    hiku.set_line1(lb_dt)
    hiku.set_line2(lb_dt)
    hiku.set_line3(lb_num_b10)
    hiku.set_line4(lb_dt)
    hiku.print_hiku()






if __name__ == "__main__":
    main()