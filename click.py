import webbrowser
import os
import random
import glob
cwd = os.getcwd()
cwd = cwd.replace("\\", "\\\\")

done = 'n'
q = '"'
##while (done == 'n'):
##    print ("to pate from your clip board, click the top left icon > edit > paste\n")
##    direc = input("paste your directory: ")
##    done = 'y'
##    break

dirlist = os.listdir(cwd)
list1 = []
with open('filenames.txt', 'w', encoding='utf8') as f:
    for item in dirlist:
        if (item == "README.txt" or item == 'README.md' or item == 'Clicky2.html' or item == 'eromanga.jpg' or item == 'click.py' or item == 'filenames.txt' or item == 'Click(folder setup).py'):
            print ("Skipping")
        else:
            f.write (q + "%s" % item + q + ", ")
            print("Writing file")
            list1.append("%s" % item)
            print(cwd)

f = open('Clicky2.html','w', encoding='utf8')


message = """
<html>
    <head>
            <style>
                body{
                    background-color: black;
                }
                .button {
        background-color: purple;
        border: none;
        color: white;
        padding: 3px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 12px;
        cursor: pointer;
        margin-top: -40px;
        margin-bottom: -90px;
        font-family: 'Courier New', Courier, monospace;
        padding-bottom: -2;
}
h1{
    font-family: 'Courier New', Courier, monospace;
    font-size: 12;
    color: white;
    float: right;
    position: relative;
    left: -200px;
    top: -10px;
    padding: 0px;
    margin: 0px;
}
h2{
    font-family: 'Courier New', Courier, monospace;
    font-size: 12;
    color: white;
    float: right;
    position: relative;
    left: -220px;
    top: -10px;
    padding: 0px;
    margin: 0px;
}

            </style>
    </head>
<body onload = "tt();">
        
        <button class = "button" onclick="clicky1()">clicky</button>
        <button class = "button" onclick="clicky2()">clicky2</button>
        <button class = "button" onclick="clicky3()">clicky3</button>
        <button class = "button" onclick="clicky4()">clicky4</button>
        <button class = "button" onclick="back()">Back</button>
        <button class = "button" onclick="forward()">Forward</button>
        <button class = "button" onclick="ca()">Clear</button>
        <button class = "button" onclick="rs()">Reset</button>
        <button class = "button" onclick="play()">Repeat</button>
        <button class = "button" onclick="replay()">Replay</button>
        
        
        <script type = "text/javascript">
            var multi = new Number(0);
            var position = 0;
            var test = "test";
            var cache = [];
            localcache = [];
            localcache2 = [];
            localcache3 = [];
            localcache4 = [];
            function tt(){
                document.getElementById("mu").innerHTML = "Repeating";
                
            }
            var ar = %s; 
            var ar2 = [];
            var ar3 = [];
            var ar4 = [];
                                                            
            
                function clicky1(Number) {
                    var randomItem = ar[Math.floor(Math.random()*ar.length)];
                    console.log(multi);
                    multi = multi;

                    var x = 0;
                    if (multi == 0){
                        document.getElementById("myFrame").src = randomItem;
                        cache.push(randomItem);
                    }
                    else{
                    

                    while (x == 0){
                        console.log("while");
                        console.log(cache.length);
                        console.log(ar.length);

                    for (i = 0; i <= localcache4.length; i++){
                        includes = localcache4.includes(randomItem);
                        console.log("for");
                        if (includes == true){
                            console.log("true");
                            if(localcache4.length >= ar.length){
                                console.log("break");
                            document.getElementById("myFrame").src = "eromanga.jpg";
                            break;
                            x = 1;
                        }
                            else{
                                
                                randomItem = ar[Math.floor(Math.random()*ar.length)];
                                console.log(test);
                                
                                
                            }
                        }
                        else{
                            document.getElementById("myFrame").src = randomItem;
                            cache.push(randomItem);
                            localcache4.push(randomItem);
                            console.log(localcache4);
                            console.log("play");
                            x = 1;
                            break;
                            
                        }
                    }
                    x = 1; 
                    break;
                    }
                }
                    
                    
                            

                    position = cache.length - 1;
                    document.getElementById("text").innerHTML = randomItem;
                    
                }
                function rs(Number){
                    document.getElementById("myFrame").src = "eromanga.jpg";
                }
                function clicky2(Number){
                    
                    var randomItem = ar2[Math.floor(Math.random()*ar2.length)];
                    console.log(multi);
                    multi = multi;

                    var x = 0;
                    if (multi == 0){
                        document.getElementById("myFrame").src = randomItem;
                        cache.push(randomItem);
                    }
                    else{
                    

                    while (x == 0){
                        console.log("while");
                        console.log(cache.length);
                        console.log(ar2.length);

                    for (i = 0; i <= localcache2.length; i++){
                        includes = localcache2.includes(randomItem);
                        console.log("for");
                        if (includes == true){
                            console.log("true");
                            if(localcache2.length >= ar2.length){
                                console.log("break");
                            document.getElementById("myFrame").src = "eromanga.jpg";
                            break;
                            x = 1;
                        }
                            else{
                                
                                randomItem = ar2[Math.floor(Math.random()*ar2.length)];
                                console.log(test);
                                
                                
                            }
                        }
                        else{
                            document.getElementById("myFrame").src = randomItem;
                            cache.push(randomItem);
                            localcache2.push(randomItem);
                            console.log(localcache2);
                            console.log("play");
                            x = 1;
                            break;
                            
                        }
                    }
                    x = 1; 
                    break;
                    }
                }
                    
                    
                            

                    position = cache.length - 1;
                    document.getElementById("text").innerHTML = randomItem;

                }
                function clicky3(Number){
                    
                    var randomItem = ar3[Math.floor(Math.random()*ar3.length)];
                    console.log(multi);
                    multi = multi;

                    var x = 0;
                    if (multi == 0){
                        document.getElementById("myFrame").src = randomItem;
                        cache.push(randomItem);
                    }
                    else{
                    

                    while (x == 0){
                        console.log("while");
                        console.log(cache.length);
                        console.log(ar3.length);

                    for (i = 0; i <= localcache.length; i++){
                        includes = localcache.includes(randomItem);
                        console.log("for");
                        if (includes == true){
                            console.log("true");
                            if(localcache.length >= ar3.length){
                                console.log("break");
                            document.getElementById("myFrame").src = "eromanga.jpg";
                            break;
                            x = 1;
                        }
                            else{
                                
                                randomItem = ar3[Math.floor(Math.random()*ar3.length)];
                                console.log(test);
                                
                                
                            }
                        }
                        else{
                            document.getElementById("myFrame").src = randomItem;
                            cache.push(randomItem);
                            localcache.push(randomItem);
                            console.log(localcache);
                            console.log("play");
                            x = 1;
                            break;
                            
                        }
                    }
                    x = 1; 
                    break;
                    }
                }
                    
                    
                            

                    position = cache.length - 1;
                    document.getElementById("text").innerHTML = randomItem;
                }
                        



                
                function clicky4(Number){
                    var randomItem = ar4[Math.floor(Math.random()*ar4.length)];
                    console.log(multi);
                    multi = multi;

                    var x = 0;
                    if (multi == 0){
                        document.getElementById("myFrame").src = randomItem;
                        cache.push(randomItem);
                    }
                    else{
                    

                    while (x == 0){
                        console.log("while");
                        console.log(cache.length);
                        console.log(ar4.length);

                    for (i = 0; i <= localcache3.length; i++){
                        includes = localcache3.includes(randomItem);
                        console.log("for");
                        if (includes == true){
                            console.log("true");
                            if(localcache3.length >= ar4.length){
                                console.log("break");
                            document.getElementById("myFrame").src = "eromanga.jpg";
                            break;
                            x = 1;
                        }
                            else{
                                
                                randomItem = ar4[Math.floor(Math.random()*ar4.length)];
                                console.log(test);
                                
                                
                            }
                        }
                        else{
                            document.getElementById("myFrame").src = randomItem;
                            cache.push(randomItem);
                            localcache3.push(randomItem);
                            console.log(localcache3);
                            console.log("play");
                            x = 1;
                            break;
                            
                        }
                    }
                    x = 1; 
                    break;
                    }
                }
                    
                    
                            

                    position = cache.length - 1;
                    document.getElementById("text").innerHTML = randomItem;

                }
                function back(Number){
                    
                    if (position <= 0){

                    }
                    else{
                    position = position - 1;
                    
                }
                    document.getElementById("myFrame").src = cache[position];
                    console.log(position);
                    console.log(cache);
                    document.getElementById("text").innerHTML = cache[position];

                }
                function forward(Number){
                    if (position >= cache.length + 1){

                 }
                else{
                position = position + 1;

                }
                document.getElementById("myFrame").src = cache[position];
                    console.log(position);
                    console.log(cache);
                    document.getElementById("text").innerHTML = cache[position];
                }
                function ca(){
                    localcache = localcache;
                    console.log(localcache);
                    console.log("Clearing");
                cache.length = 0;
                localcache.length = 0;
                localcache2.length = 0;
                localcache3.length = 0;
                localcache4.length = 0;
                console.log(cache);
                
                }
                function play(Number){
                    console.log(multi);
                    if (multi == 0){
                        multi = 1
                        document.getElementById("mu").innerHTML = "Not repeating";
                    }
                    else{
                        multi = 0;
                        document.getElementById("mu").innerHTML = "Repeating";
                    }
                    
                }
                function replay(){
                    document.getElementById("myFrame").src = cache[position];
                }

                </script>
                <h1><p id = "text"></p></h1>
                <h2><p id = "mu"></p></h2>
<p id ="test">
        <OBJECT classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,0,0" WIDTH="100%%" HEIGHT="96%%" id="MyLink" ALIGN="">
            <PARAM NAME=movie VALUE="" id ="myLink"> <PARAM NAME=quality VALUE=high>  <EMBED src = "eromanga.jpg" id="myFrame" quality=high WIDTH="100%%" HEIGHT="96%%" NAME="" ALIGN="" TYPE="application/x-shockwave-flash" PLUGINSPAGE="http://www.macromedia.com/go/getflashplayer"></EMBED> </OBJECT>


               

            </p>
</body>
</html>
""" 
dd  = message % (list1)
f.write(dd)
f.close()
