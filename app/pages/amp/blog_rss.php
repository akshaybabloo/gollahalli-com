<?php
function blog()
{
    $url = "https://blog.gollahalli.me/rss/";
    $content = file_get_contents($url);

    $x = new SimpleXmlElement($content);
    $ret = '';
    foreach ($x->channel->item as $entry) {
        $media = $entry->children('media', True);

        $ret .= "<a href='$entry->link' class='blog-carousel-item'>";

        if ($media) {
            $url = $media->content->attributes();
            $ret .= "<amp-img  src=" . addScheme($url). " width=125 height=150></amp-img>";
        }else{
            $ret .= "<amp-img  src='#' width=125 height=150></amp-img>";
        }

        $ret .= "<div class='blog-carousel-item-caption'>";
        $ret .= "<h5 class='margin-0'>".$entry->title."</h5>";
        $ret .= "<small>Read more...</small>";
        $ret .= "</div></a>";
    }
    return $ret;
}