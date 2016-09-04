<?php

foreach ($results->publication as $key => $jsons) {
    echo '<h3>' . ucwords($key) . '</h3>';
    echo '<hr>';
    echo '<ol class="text-justify">';
    foreach ($jsons as $value) {
        echo '<li>' . $value . '</li>';
    }
    echo '</ol>';
}