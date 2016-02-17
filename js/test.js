function usd_to_eur( amount ) {
	// Convert dollars to euros
	return Math.round(amount * 0.9)
}


function eur_to_usd( amount ) {
	// Convert euros to dollars
	return Math.round(amount * 1.12)
}


function mul_to_usd( amount ) {
	// Convert multiple different US values to euros
	return amount.map(money => usd_to_eur(money))
}


function mul_to_eur( amount ) {
	// Convert multiple different EU values to dollars
	return amount.map(money => eur_to_usd(money))
}


QUnit.test( "hello test", function( assert ) {
  assert.ok( 1 == "1", "Passed!" );
});

QUnit.test( "Convert USD to EUR", function( assert ) {
	assert.ok( usd_to_eur(20) == 18, "Passed!");
	assert.ok( usd_to_eur(150) == 135, "Passed!");
	assert.ok( usd_to_eur(10000) == 9000, "Passed!");
});

QUnit.test( "Convert EUR to USD", function( assert ) {
	assert.ok( eur_to_usd(42) == 47, "Passed!");
	assert.ok( eur_to_usd(284) == 318, "Passed!" );
	assert.ok( eur_to_usd(999) == 1119, "Passed!" );
});

QUnit.test( "Convert multiple USD to EUR", function( assert ) {
	assert.ok( mul_to_usd([7, 100, 823]), [6, 90, 741]);
});

QUnit.test( "Convert multiple EUR to USD", function( assert ) {
	assert.ok( mul_to_eur([9, 184, 754]), [10, 207, 844]);
})