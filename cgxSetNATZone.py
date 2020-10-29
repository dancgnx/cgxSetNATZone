#!/usr/bin/env python

import cloudgenix_settings
import cloudgenix
from cloudgenix import jd, jd_detailed
import cgxinit
import logging
import sys

if __name__ == "__main__":

    # read args and initiate authenticated cloudgenix SDK instance
    cgx, args = cgxinit.go()
    cloudgenix.api_logger.setLevel(logging.WARN)
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("requests").setLevel(logging.WARN)
    logging.getLogger("urllib3").setLevel(logging.WARN)
    log = logging.getLogger("cgxSetNATZone")


    # create element database
    elements = {}
    for element in cgx.get.elements().cgx_content["items"]:
        elements[element['name']] = element

    if args['list_elements']:
        for element in elements:
            print(element)
            sys.exit()

    # find the target zone ID
    for natzone in cgx.get.natzones().cgx_content['items']:
        if natzone['name'] == args['zone']:
            natzone_id = natzone['id']
            break
    else:
        log.error(f"NAT zone {args['zone']} not found")
        sys.exit()

    # retrieve a list of element names
    if args["elements"]:
        # read a list of elements from a file if not remarks or empty
        elements_names = [
            element.strip()
            for element in args["elements"].readlines()
            if element[0] != "#" and element.strip() != ""
        ]
    elif args["element"]:
        elements_names =args["element"]
    else:
        log.error("--element or --elements is requried. Use -h for help")
        sys.exit()

    # for each element in the list and for each interface in the element update the NAT zone
    for element in cgx.get.elements().cgx_content['items']:
        # search for name in the element list
        if element['name'] in elements_names:
            #element found save some basic info and print a message
            e_name = element['name']
            e_id = element['id']
            e_site_id = element["site_id"]
            log.info(f"Working on {e_name}")

            # scan elements interface and match interface name to the list of interfaces
            for interface in cgx.get.interfaces(e_site_id, e_id).cgx_content['items']:
                if interface['name'] in args['interface']:
                    log.info(f"----- Updating interface {interface['name']}")
                    # interface found update the zone
                    interface['nat_zone_id'] = natzone_id

                    #update interface
                    res = cgx.put.interfaces(e_site_id, e_id, interface['id'], interface)
                    if not res:
                        log.error("---------- Failed to update interface")
                        jd_detailed(res)
                        sys.exit()
                    log.info("---------- Success")



