<html>
<body>
    <head>
    <link rel="stylesheet" href="main.css">
</head>
 <form action="index.php" class="authform" method="post" accept-charset="utf-8">
        <fieldset>
            <legend>Show me the way</legend>
            <input type="text" id="choice" name="choice" value="" placeholder="The_Choice" />
            <input type="text" id="hash" name="hash" value="" placeholder="The_Hash" />
            <input type="submit" name="submit" value="Let's see" />

        <div class="return-value" style="padding: 10px 0">&nbsp;</div>
        </fieldset>
        </form>
<?php
require('flag.php');
function gen_random() { //Sheeeeeeesh, a random number, NO BRUTE FORCE baby
    $a = rand(106,2684532105898);
    $b = rand(69,12469200035888);
    return $a+$b;
}
if (isset($_GET['source'])) {
    show_source(__FILE__);  //OKKKKKKKKKKKKK, i'll help you, still not enough to break me.
    die();
}
if (isset($_POST['choice']) && isset($_POST['hash'])) {
    $choice = $_POST['choice'];
    $hash = $_POST['hash'];
    $salt='1237';
    $salted_hash = hash('md5', $salt . $hash);
    $r = gen_random();
    if($choice != false && $salted_hash != false) {
        if($choice.$r == $salted_hash) {
            echo "<legend>I lost, here is your prize: </legend>" ;
            echo "<legend>";
            echo getFlag();
            echo "</legend>";
            
        }
        else {
            echo "<legend>Hehehehehehehehe</legend>";
        }
    }
    else {
        echo "<legend>It doesn't work like that man...</legend>";
    }
}
?>
<p><em><a href="index.php?source">source code</a></em></p>
</body>
</html>
