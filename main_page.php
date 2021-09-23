<!DOCTYPE html>
<?php session_start(); ?>
<html>
    <head>
        <meta http-equiv="content-type" content="text/html; charset=utf-8">
        <link href="css/style.css" rel="stylesheet" type = "text/css"/>
        <title>SOS</title>
        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
        <script src = "js/script.js"></script>
        <script type="text/javascript" src="js/extraction.js"></script>
        <script src="https://cdn.zingchart.com/zingchart.min.js"></script>
    </head>

    <body>
        <div class="container">
            <header>
                <h1><img src="images/logo.png" width="456" height="190"></h1>
                <nav>
                     <ul class = "userMenu">
                       <?php
                       if(!isset($_SESSION['user_id']) || !isset($_SESSION['user_name'])) {
                         echo "<li><a href='../sign_in.html'>SIGN IN &nbsp;&nbsp;</a></li>";
                         echo "<li><a href='../sign_up.html'>SIGN UP &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a></li>";
                       } else {
                         $user_id = $_SESSION['user_id'];
                         $user_name = $_SESSION['user_name'];
                         echo "<li><a href=''>Welcome $user_id</a></li>";
                         echo "<li><a href='php/sign_out.php'>SIGN OUT</a></li>";
                       }
                       ?>
                     </ul>

                     <ul class = "mainMenu">
                        <li><a href="main_page.php">Video Report</a></li>
                        <li><a href="php/premium.php">Premium</a></li>
                        <li><a href="">Community</a></li>
                    </ul>
                </nav>
            </header>

            <section class = "main">
                <div class = search>
                    <input class="input" type="text" id = "URL" placeholder="Input Video URL">
                    <input class="button" type="button" id = "bt" value= "search" onclick = "searchURL()">
                </div>
                <h1 id="intro"><img src="images/report.png" width ="1000" height = "140"></h1>

                <section id = "afterSearch"> <!--URl search 후 나타나는 화면-->
                    <div id = "video">
                      <p align = "middle"><iframe id="source" src = "" width="478" height="269"></iframe></p>
                    </div>
                    <div id="Progress_Loading">
                         <progress value="0" max="100" id="pg"></progress><span id="percent"> 0%</sapn>
                    </div>
                    <!--tap기능 구현-->
                   <div class = "tabWrap">
                        <div class = "tabMenu">
                            <button class = "tabButton On" onclick = "openTab(event, 'tab1')">Highlight</button>
                            <button class = "tabButton" onclick ="openTab(event, 'tab2')" >Keyword</button>
                        </div>
                        <div class = "tabResult_container">
                            <div class = "tabResult" id ="tab1" style= "display : block">
                              <div>
                                <b>From:</b>
                                <span id="date-from">1/31/19</span>
                                <b> To:</b>
                                <span id="date-to">6/17/19</span>
                              </div>
                              <div id="myChart" class="chart--container">
                                <div id="main-container">
                                  <a class="zc-ref" href="https://www.zingchart.com/">Powered by ZingChart</a>
                                </div>
                              </div>
                              <script type="text/javascript" src="js/chart.js"></script>
                            </div>
                            <div class = "tabResult" id ="tab2" style = "display : none; background-image:URL('images/keyword_chart_win.png');" >
                        </div>
                    </div>
                </section>
            </section>
        </div>
    </body>
</html>
