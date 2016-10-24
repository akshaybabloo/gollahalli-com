<?php
foreach ($results->skills as $key1 => $jsons1) {
    echo '<div class="col-sm-6">';
    echo '<div class="table-responsive">';
    echo '<table class="table table-hover borderless">';
    echo '<tbody>';
    foreach ($jsons1 as $key2 => $jsons2) {
        $header = true;
        foreach ($jsons2 as $value) {
            echo '<tr>';
            echo ($header) ? '<td class="col-md-2">' . ucfirst($key2) . '</td class="col-md-2">' : '<td class="col-md-2"></td class="col-md-2">';
            echo '<td class="col-md-1">' . ucfirst($value) . '</td class="col-md-1">';
            echo '</tr>';
            $header = false;
        }
    }
    echo '</tbody>';
    echo '</table>';
    echo '</div>';
    echo '</div>';
}
