# heart_rate_sentinel_server

To run the server, first run the hr_server.py file, which starts up the server. Then, to validate the patient info POST modules, run callserver.py and then callserverhr.py. To validate the other modules, you can then run call_hr_patid.py, call_status_patient.py, call_hr_av.py, and call_hr_int_av.py in any order. In order to run any of these last four "call" files, the first two "call" files mentioned previously have to have been ran and in the right order. These call files output what is being returned in each of the respective modules for the specific server address.


The time somehow seems to be in Greenwich Mean Time. The actual number date and time is correct with our time zone but it is followed by GMT, so Python somehow thinks I am in that time zone. I'm not sure how to fix this, but I don't think it's a big deal, so I am leaving the times in GMT. 


I did have sufficient time to finish this project, so I did not get sendgrid to work or use a vcm. I tried to implement the sendgrid code but never got it to run as it should. I left my tester sendgrid code in the hr_server.py file and commented it out. I also removed my API key. In addition, I was not able to write sufficient test coverage or get the interval average portion of the server to work correctly. 
