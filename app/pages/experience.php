<?php

function experience()
{
    global $results, $cdn;
    $ar = array();
    $ret = '';
    foreach ($results->experience as $jsons) {
        array_push($ar, $jsons);
    }

    foreach (array_reverse($ar) as $j) {
            $ret .= '<div class="cd-timeline-block">';
            if ($j->current) {
                $ret .= '<div class="cd-timeline-img cd-picture">';
            } else {
                $ret .= '<div class="cd-timeline-img cd-movie">';
            }
            $ret .= '<img src="'. $cdn .'/assets/img/grad.png" alt="Grad-pic">
                        </div>
                        <div class="cd-timeline-content">';
            $ret .= '<h4>' . $j->title . '</h4>';

            $ret .= '<p class="text-muted">' . $j->company . '<br>'. $j->where . '</p>';
            $ret .= '<span class="cd-date">' . $j->from . ' - ' . $j->to . '</span>';
            $ret .= '</div></div>';
        }
    return $ret;
}
