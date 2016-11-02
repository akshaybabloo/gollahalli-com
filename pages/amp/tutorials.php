<?php

function tutorials()
{
    global $results, $cdn;
    $ret = '';

    foreach ($results->tutorials as $jsons) {
        $ret .= "<a href='$jsons->link' class='blog-carousel-item'>";
        $ret .= "<amp-img  src='. $cdn . '/img/portfolio/' . $jsons->title . '.jpg' width=125 height=150></amp-img>";
        $ret .= "<div class='blog-carousel-item-caption'>";
        $ret .= "<h5 class='margin-0'>" . $jsons->title . "</h5>";
        $ret .= "<small>Read more...</small>";
        $ret .= "</div></a>";
    }
    return $ret;
}