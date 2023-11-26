Title: Why use AWS glacier
Date: 2023-10-01 19:20
Modified: 2023-10-01 19:20
Category: icechest
Tags: AWS,python,glacier,icechest
Slug: Why use AWS glacier
Authors: Timothy Lee
Summary: Thoughts about why AWS glacier made sense for icechest.

Why use Amazon Glacier as the backend for IceChest? Well at $0.0036 per GB / Month it has extremely low cost per GB stored. Compare for example to Apple's iCloud storage which costs $2.99 / Month for 200GB, which would cost $0.72 in Glacier. True Glacier does charge around $0.01 / GB to retrieve data, but I think for most people who want to backup their pictures or videos that shouldn't be too much of a burden. Glacier is also extremely reliable.
