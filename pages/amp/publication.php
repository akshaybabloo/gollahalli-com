<?php

function publications()
{
    global $results;
    $ret = '';
    foreach ($results->publication as $key => $jsons) {
        $ret .= '<h3>' . ucwords($key) . '</h3>';
        $ret .= '<ol class="text-justify">';
        foreach ($jsons as $value) {
            $ret .= '<li>' . $value . '</li>';
        }
        $ret .= '</ol>';
    }
    return $ret;
}