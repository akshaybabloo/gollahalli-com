<?php
$json_skills = file_get_contents('pages/content.json');

$results_skills = json_decode($json_skills);

foreach ($results_skills->skills as $key => $jsons) {
    foreach ($jsons as $value) {
        echo '<tr>';
        echo '<td class="col-md-2">'.ucwords($key).'</td>';
        echo '<td class="col-md-1">' . $value . '</td>';
        echo '</tr>';
    }
}