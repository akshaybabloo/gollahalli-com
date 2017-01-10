<?php
function blog()
{
    $feed = new SimplePie();
    $feed->set_feed_url('https://blog.gollahalli.me/?format=rss');
    $feed->enable_cache(false);
    $feed->init();
    $feed->handle_content_type();

    $ret = '';

    try {
        foreach ($feed->get_items() as $entry) {

            $ret .= "<a href=".$entry->get_permalink()." class='blog-carousel-item'>";

            if ($enclosure = $entry->get_enclosure()) {
                if (!$enclosure->get_link() == "") {
                    $ret .= "<amp-img  src=" . addScheme($enclosure->get_link()) . " width=125 height=150></amp-img>";
                } else {
                    $ret .= "<amp-img  src='#' width=125 height=150></amp-img>";
                }
            }

            $ret .= "<div class='blog-carousel-item-caption'>";
            $ret .= "<h5 class='margin-0'>" . $entry->get_title() . "</h5>";
            $ret .= "<small>Read more...</small>";
            $ret .= "</div></a>";
        }
    } catch (Exception $e){
        $ret = 'Under Maintenance';
    }
    return $ret;
}