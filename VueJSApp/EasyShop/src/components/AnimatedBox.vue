<template>
    <div id="animated-back">
          <h1> Easy Shop<br/> anytime...anywhere...always!</h1>
    </div>
</template>

<script></script>

<style>
@import url(https://fonts.googleapis.com/css?family=Kaushan+Script);

#animated-back {
  background: -webkit-radial-gradient(circle, #8cff66, #fff);
  height: 100%;
  margin: 0;
  padding: 0;
  display: flex;
  align-items: center;
  justify-content: space-around;
}

h1 {
  font-family: "Kaushan Script";
  text-align: center;

  border-top: solid #005ce6 3.9px;
  border-bottom: solid #005ce6 5.9px;

  padding: 0;
  overflow: hidden;
  animation: animateHeading 3s forwards;
}

h3 {
  font-family: "Kaushan Script";
  text-align: right;

  border-bottom: solid black 2.9px;
  padding: 0;
  overflow: hidden;
}
@keyframes animateHeading {
  0% {
    transform: rotate(90deg);
    width: 0;
    height: 0;
  }
  20% {
    transform: none;
    width: 25%;
    height: 0;
  }
  40%,
  80% {
    width: 25%;
    height: 1.4em;
  }
  100% {
    width: 70%;
    height: 3.11em;
  }
}
</style>