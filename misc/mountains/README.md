# Mountains

Took this pretty cool picture on a mountain, can you find where this is?

Flag should be name of the mountain followed by its elevation in meters.
Format:
`gigem{name_altitude}`

Author: Emmie

## Solution

We get an image with an image of a mountain and what appears to be some trees, people walking, and a stone structure, and are asked to find the location of the image.

If we perform a Google reverse image search, which is done by going to Google Images and selecting "Search By Image", then we see that the stone structure appears to match with a link discussing Sandia Mountains, whose image also appears to have a similar stone structure. Upon going to the link, we can get a closer look at the stone structure, which we find to be "Kiwanis Cabin", and since the stone structure and environment appears to be the same, we can confirm that Sandia Mountains is in fact the mountain in the image.

Knowing this, we have solved half of the challenge, which is determining the name of the mountain, which is Sandia. We now need to find the elevation. If we go to the Wikipedia page for "Sandia Mountains", we find the highest point of the mountain, Sandia Crest, to be listed as at elevation 3255 meters. As such, we now know both the name of the mountain and the elevation, meaning we have solved the challenge. 

flag:
`gigem{sandia_3255}`
