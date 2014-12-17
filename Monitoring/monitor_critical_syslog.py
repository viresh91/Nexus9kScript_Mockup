"""Script Cataloging Information
:Product Info:Nexus::9000::9516::NX-OS Release 6.2
:Category:Monitoring
:Title:Critical Syslog Monitoring
:Short Description:This script to monitor Critical Syslog Errors.
:Long Description:This Script to monitor monitor critical Syslog errors like 
Alerting and take action. 
Example: ( ospf adj flapping more than X times in Y duration, cost out the link).
:Input:Syslog ID
:Output:Critical Syslog Error Status.
"""

import os

def main():
    """
    This method will do the monitoring functionality 
    """
    print "Printing Status"


if __name__ == '__main__':
    main()
