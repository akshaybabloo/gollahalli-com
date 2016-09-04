<?php

foreach ($results->skills as $key => $jsons) {
    foreach ($jsons as $value) {
        echo '<tr>';
        echo '<td class="col-md-2">'.ucwords($key).'</td>';
        echo '<td class="col-md-1">' . $value . '</td>';
        echo '</tr>';
    }
}