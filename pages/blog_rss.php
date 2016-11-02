<?php

function blog()
{
    $url = "https://blog.gollahalli.me/rss/";
    $content = file_get_contents($url);

    $x = new SimpleXmlElement($content);
    $ret = '';
    foreach ($x->channel->item as $entry) {
        $ret .= "<div class='mas-container mas-col3'><div class='grid-sizer'></div><div class='blog-item3 item'>";
        $nameSpace1 = $entry->getNameSpaces(True);
        $media = $entry->children('media', True);
        $dc = $entry->children($nameSpace1['dc']);
        $newDateString = date_format(date_create_from_format('D, d M Y G:i:s T', $entry->pubDate), 'd M Y');

        if ($media) {
            $url = $media->content->attributes();
            $ret .= "<img class='hover_style3' src=' " . addScheme($url) . " ' alt='$entry->title'>";
        }

        $ret .= "<div class='top-bar'><span><strong><i class='ion-person-stalker'></i></strong>" . " " . $dc->creator . "</span><span><i class='ion-clock'></i>" . " " . $newDateString . "</span></div>";
        $ret .= "<a href='$entry->link' title='$entry->link'><h4><b>" . $entry->title . "</b></h4></a>";
        $ret .= "<p>" . $entry->description . "</p>";
        $ret .= "<div class='blog_readmore_btn_holder'><a href='$entry->link' class='more-link'><div class='blog_readmore_btn3'>" . "Continue reading" . "<i class='ion-arrow-right-c'></i></div></a></div>";
        $ret .= "</div></div>";
    }
    return $ret;
}
