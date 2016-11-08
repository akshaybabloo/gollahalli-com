<?php require 'pages/error/header.php' ?>
    <title>Forbidden</title>


</head>
<body data-gr-c-s-loaded="true">
<div class="wrapper">
    <div class="container">
        <?php echo header_image(); ?>

        <div class="content-primary">
            <h1 class="title">System Overload</h1>
            <p class="description">The server cannot process your request due to a system overload; this is a temporary problem.</p>
            <div class="section-footer">
                <a href="https://www.gollahalli.me" class="button button-primary">Back To Homepage</a>
                <a href="mailto:akshay@gollahalli.me?Subject=System%20overload%20error" class="button button-default">Report Error</a>
            </div>
        </div>
    </div>

    <?php require 'pages/error/footer.php' ?>
