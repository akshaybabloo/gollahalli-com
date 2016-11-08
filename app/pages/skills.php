<?php
function skills()
{
    global $results;
    $ret = '';
    foreach ($results->skills as $key1 => $jsons1) {
        $ret .= '<div class="col-sm-6">';
        $ret .= '<div class="table-responsive">';
        $ret .= '<table class="table table-hover borderless">';
        $ret .= '<tbody>';
        foreach ($jsons1 as $key2 => $jsons2) {
            $header = true;
            foreach ($jsons2 as $value) {
                $ret .= '<tr>';
                $ret .= ($header) ? '<td class="col-md-2">' . ucfirst($key2) . '</td class="col-md-2">' : '<td class="col-md-2"></td class="col-md-2">';
                $ret .= '<td class="col-md-1">' . ucfirst($value) . '</td class="col-md-1">';
                $ret .= '</tr>';
                $header = false;
            }
        }
        $ret .= '</tbody>';
        $ret .= '</table>';
        $ret .= '</div>';
        $ret .= '</div>';
    }
    return $ret;
}
