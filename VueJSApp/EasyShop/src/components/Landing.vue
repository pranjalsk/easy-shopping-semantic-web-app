<template>
<div>
<nav>
	<ul>
		<li><a href="#">Home</a></li>
		<li><a href="#">Product Nutrients Info</a></li>
		<li><a href="#">Wallmart</a>
			<ul>
				<li><a href="#">Locations</a></li>
				<li><a href="#">Products</a>
					<ul>
						<li><a href="#">Bakery</a></li>
						<li><a href="#">Dairy</a></li>
						<li><a href="#">Seafood and Meat</a></li>
						<li><a href="#">Beer and Wine</a></li>
						<li><a href="#">Fruits and Vegetable</a></li>
					</ul>
				</li>
			</ul>
		</li>
		<li><a href="#">Safeway</a>
			<ul>
				<li><a href="#">Locations</a></li>
				<li><a href="#">Products</a>
					<ul>
						<li><a href="#">Bakery</a></li>
						<li><a href="#">Dairy</a></li>
						<li><a href="#">Seafood and Meat</a></li>
						<li><a href="#">Beer and Wine</a></li>
						<li><a href="#">Fruits and Vegetable</a></li>
					</ul>
				</li>
			</ul>
		</li>
	</ul>
</nav>
</div>
</template>



<script>
export default {};
</script>

<style>
nav {
  text-align:center;
	color: #fff;
  width: 100%;
  background: #00802b;
  padding: 0;
  margin: 0;
  height: 60px;
  position:relative;
}

nav ul {
  background: #00802b;
	color: #fff;
  list-style:none;
  padding:0 20px;
  margin: 0;
  height: 60px;

}


nav ul li {
  display: inline-block;
}


nav ul li a {
  color:#00802b;
	color: #fff;
  display:block;
  padding:0px 40px;
  text-decoration:none;
  float: left;
  height: 60px;
   line-height: 60px;
}

nav ul li:hover {
  background: #333333;
}


nav ul li:hover > a{
    color:#FFFFFF;
}

nav ul li:hover > ul {
  display:block;
}

nav ul ul {
  background: #00802b;
  padding:0;
  text-align: center;
  display:none;
    width: 100%;
  position: absolute;
  top: 60px;
  left: 0px;
}

</style>
