import pytest


class Test_roombr:

    @pytest.mark.daily
    @pytest.mark.feed_post
    def test_one(self):
        """Test login functionality for two users and initialize the third."""
        print("one ")
        assert 11 == 11

    @pytest.mark.activities
    @pytest.mark.feed_post
    def test_second(self):
        print("second time ")
        assert 22 == 11

    @pytest.mark.activities
    def test_third(self):
        print("third time ")
        assert 33 == 33

    @pytest.mark.feed_post
    def test_four(self):
        print("four time ")
        assert 54 == 54
