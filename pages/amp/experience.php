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
        $ret .= '<div class="time-line-item">';
        $ret .= '<amp-img ';
        if ($j->current) {
            $ret .= 'class="yes-true"';
        } else {
            $ret .= 'class="no-false"';
        }
        $ret .= ' src="'. $cdn .'/img/grad.png"
                width="30"
                height="30"
                layout="fixed"
                attribution="Grad-pi"
                on="tap:timeline_lightbox_1"
                role="button"
                tabindex="0"></amp-img>';

        $ret .= '<h4 class="margin-0">' . $j->title . '<small>'. ' ' . $j->from . '-'. $j->to .'</small></h4>';
        $ret .= '<p class="margin-0">' . $j->company . '<br>'. $j->where . '</p>';
        $ret .= '</div>';
        }
    return $ret;
}
