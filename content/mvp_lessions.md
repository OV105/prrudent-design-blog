Title: Further thoughts on Minimum Viable Product
Date: 2023-11-17 10:20
Modified: 2023-11-17 19:30
Category: python
Tags: AWS,python,glacier
Slug: 
Authors: Timothy Lee
Summary: Why is shipping a MVP so hard.

It seems like the **minimum viable product** concept is very simple and should be easy to follow. However it is surprisingly hard to follow in practice. One reason is that on persons optional feature is someone else's vital feature. One recent example occurred with my project icechest.  In the upload to AWS glacier feature I had added functionality to calculate the checksum of the zip file without really thinking about it. But afterward I thought is the checksum absolutely necessary. It's certainly an important feature, but would icechest be a usable application without it. After I thought about it I realized that icechest would be usable without the checksum, but it's so hard sometimes to differentiate between really important and the absolutely necessary.
