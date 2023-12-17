# Memes Hub

## Write-up

From the Dockerfile we can see that flag.txt is copied to the root directory and the only way to get it is to read the content of the file or download it.  
The application uses os.path.join() function to get the meme path to download it, if we check the definition of this function we will see that if the second part is an absolute path, the first part will be discarded.  
To get the flag we need to send a query param `?file=/flag.txt`.

## Flag

`shellmates{J01N_4bS0lut3_pATh_F0R_LFI}`
