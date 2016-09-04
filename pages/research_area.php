<?php
echo '<ul>';
foreach ($results->research_area as $jsons) {
    echo '<li>' . $jsons . '</li>';
}
echo '</ul>';