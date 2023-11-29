Title: Patience is important
Date: 2023-11-18 17:15
Modified: 2023-11-18 17:15
Category: python
Tags: AWS,python,glacier,mvp
Slug: patience 
Authors: Timothy Lee
Summary: The asynchronous nature of AWS glacier means that you have to be patient.

It has been several hours since this job was initiated to get a list of the vault contents, but still waiting...

```
aws glacier get-job-output --account-id - --vault-name "TestOne"   --job-id "2hZR1C72YZWSHYNzF_lHtcRdBOE9YetsFBtzkqfmufrUG5__dHUZwveP9gB4p1TGXplr96_m0Qq71YXfdSOdpzg8UK-iO" job-output.txt

An error occurred (InvalidParameterValueException) when calling the GetJobOutput operation: The job is not currently available for download: 2hZRC72YZWSHYNzF_lHtcRdBOE9YetsFBtzkqfmufrUG5__dHUZwveP9gB4p1TGXplr96_m0Qq71YXfdSOdpzg8UK-iO
```
However this also means that the MVP will have to include tracking jobs. I had thought I would not have to include that feature in the MVP.
