<?php
$json = file_get_contents('pages/content.json');

$results1 = json_decode($json);

foreach ($results1->publication as $key => $jsons) {
    echo '<h3>' . ucwords($key) . '</h3>';
    echo '<hr>';
    echo '<ol class="text-justify">';
    foreach ($jsons as $value) {
        echo '<li>' . $value . '</li>';
    }
    echo '</ol>';
}