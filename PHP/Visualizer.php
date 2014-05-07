<?php

class Visualiser
{
    /**
     * @param string $text
     * @param array $pixels
     */
    public static function Draw($text, $pixels)
    {
        $rc = ceil(sqrt(count($pixels)));
        $dt = [' ', '.','"', '*',':','%','#','X'];
        $dc = count($dt);

        echo PHP_EOL, "[ $text ]", PHP_EOL;
        echo '+', str_repeat('--', $rc), '+';
        foreach ($pixels as $i => $px) {
            if ($i % $rc == 0) {
                echo $i ? '|' : '', PHP_EOL, '|';
            }
            echo str_repeat($dt[$px % $dc], 2);
        }
        echo '|', PHP_EOL, '+', str_repeat('--', $rc), '+', PHP_EOL;
    }
}
