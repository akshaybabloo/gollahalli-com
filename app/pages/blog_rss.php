<?php

function blog()
{
    $feed = new SimplePie();
    $feed->set_feed_url('https://blog.gollahalli.me/?format=rss');
    $feed->enable_cache(false);
    $feed->init();
    $feed->handle_content_type();

    $ret = '';
    $bol = true;

    try {
        foreach ($feed->get_items() as  $entry) {
            $ret .= "<div class='mas-container mas-col3'><div class='grid-sizer'></div><div class='blog-item3 item'>";
            $newDateString = $entry->get_date('j F Y | g:i a');

            if ($enclosure = $entry->get_enclosure())
            {
                if(!$enclosure->get_link() == ""){
                    $ret .= "<img class='hover_style3' src=' " . $enclosure->get_link() . " ' alt=" . $entry->get_title() . ">";
                }
            }

            $ret .= "<div class='top-bar'><span><strong><i class='ion-person-stalker'></i></strong>" . " " . $feed->get_author() . "</span><span><i class='ion-clock'></i>" . " " . $newDateString . "</span></div>";
            $ret .= "<a href=". $entry->get_permalink() . " title=". $entry->get_permalink() . "><h4><b>" . $entry->get_title() . "</b></h4></a>";
            $ret .= "<p>" . $entry->get_description() . "</p>";
            $ret .= "<div class='blog_readmore_btn_holder'><a href=". $entry->get_permalink() . " class='more-link'><div class='blog_readmore_btn3'>" . "Continue reading" . "<i class='ion-arrow-right-c'></i></div></a></div>";
            $ret .= "</div></div>";
        }
    } catch (Exception $e) {
        $ret = 'Under Maintenance';
        $bol = false;
    }
    $array = ["ret" => $ret, "bol" => $bol];
    return $array;
}