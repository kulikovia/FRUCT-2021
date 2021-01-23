import xml.etree.ElementTree as xml
import random
from random import randrange
from datetime import datetime
from datetime import timedelta
import csv

def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

d1 = datetime.strptime('2/1/20 00:00:00', '%m/%d/%y %H:%M:%S')
d2 = datetime.strptime('2/3/20 23:59:59', '%m/%d/%y %H:%M:%S')

#print(random_date(d1, d2))

Max_Devices = 9
Max_Users = 9

SPARQL_path = "C:/Blazegraph/1"

class rule:

    def start(self, interval_id, service, probability):
        self.interval_id = interval_id
        self.service = service
        self.probability = probability





def createXML():
    """
    Создаем XML файл.
    """


#Open SPARQL file
    f = open("Predictions.nq", "wt")

# Add header
    header = str("<?xml version='1.0' encoding='UTF-8'?>\n<rdf:RDF\nxmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'\nxmlns:vCard='http://www.w3.org/2001/vcard-rdf/3.0#'\nxmlns:my='http://127.0.0.1/bg/ont/test1#'\n>")
    f.write(header)

# Add Prediction nodes
    k = 0
    for j in range(Max_Devices-1):
        i = 0
        rules = []
        with open('STB_1.csv') as f_obj:
            reader = csv.DictReader(f_obj, delimiter=',')
            for line in reader:
                rules.append(rule())
                rules[i].interval_id = line["INTERVAL_ID"]
                rules[i].service = line["SERVICE"]
                rules[i].probability = line["PROBABILITY"]
                if float(rules[i].probability) >= random.randint(0, 1):
                    switcher = "ON"
                else:
                    switcher = "OFF"
                #print(rules[i].interval_id, rules[i].service, rules[i].probability)
                #body = str("\n<rdf:Description rdf:about = 'http://127.0.0.1/Request_U") + str(i) + str("/'>\n<my:request_timestamp rdf:datatype = 'http://www.w3.org/2001/XMLSchema#datetime'>") + str(random_date(d1, d2).strftime("%Y-%m-%dT%H:%M:%S")) + str("</my:request_timestamp>\n<my:request_geodata><rdf:Description rdf:about = '") + str(random.choice(reg)) + str("'></rdf:Description></my:request_geodata>\n<my:has_req_type>USER_ACTION</my:has_req_type>\n<my:request_detailes>\n<rdf:Description>\n<rdf:type>:statement</rdf:type>\n<rdf:predicat>:is_requested_with</rdf:predicat>\n<rdf:subject>") + str(random.choice(j)) + str("</rdf:subject>\n<rdf:object><rdf:Description rdf:about = 'http://127.0.0.1/Asset_") + str(random.randint(1,Max_Assets)) + str("/'></rdf:Description></rdf:object>\n</rdf:Description>\n</my:request_detailes>\n<my:requests>\n<rdf:Description rdf:about = 'http://127.0.0.1/User_") + str(random.randint(1, Max_Users)) + str("/' >\n</rdf:Description>\n</my:requests>\n</rdf:Description>\n")
                body = str("\n<rdf:Description rdf:about = 'http://127.0.0.1/Prediction_") + str(k) + str("/'>\n<my:prediction_timestamp>2020-11-19T") + str(rules[i].interval_id) + str(":00:00</my:prediction_timestamp>\n<my:has_state_type>Servise_is_used</my:has_state_type>\n<my:has_state_value>") + str(switcher) + str("</my:has_state_value>\n<my:prediction_detailes>\n<rdf:Description>\n<rdf:type>:statement</rdf:type>\n<rdf:predicat>:use_prediction_rules</rdf:predicat>\n<rdf:subject><rdf:Description rdf:about = 'http://127.0.0.1/STB_") +str(j) + str("/'></rdf:Description></rdf:subject>\n<rdf:object>") + str(rules[i].service) + str("</rdf:object>\n</rdf:Description>\n</my:prediction_detailes>\n</rdf:Description>\n")
                f.write(body)
                i = i + 1
                k = k + 1

    f.write("\n</rdf:RDF>\n")

    f.close()

if __name__ == "__main__":
    createXML()
