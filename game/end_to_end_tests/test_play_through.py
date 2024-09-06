import pytest

from .base_game_test import BaseGameTest


class TestPlayThrough(BaseGameTest):
    def setUp(self):
        self.login_once()

    def _complete_episode(
        self, episode_number, level_number, from_python_den=False, **kwargs
    ):
        page = self.go_to_episode(episode_number)
        self.complete_and_check_level(
            level_number, page, from_python_den, **kwargs
        )

    def _complete_level(self, level_number, from_python_den=False, **kwargs):
        page = self.go_to_level(level_number, from_python_den)
        self.complete_and_check_level(
            level_number, page, from_python_den, **kwargs
        )

    def test_episode_01(self):
        self._complete_episode(1, 1, check_algorithm_score=False)

    def test_level_001(self):
        self._complete_level(1, check_algorithm_score=False)

    def test_level_002(self):
        self._complete_level(2, check_algorithm_score=False)

    def test_level_003(self):
        self._complete_level(3, check_algorithm_score=False)

    def test_level_004(self):
        self._complete_level(4, check_algorithm_score=False)

    def test_level_005(self):
        self._complete_level(5, check_algorithm_score=False)

    def test_level_006(self):
        self._complete_level(6, check_algorithm_score=False)

    def test_level_007(self):
        self._complete_level(7, check_algorithm_score=False)

    def test_level_008(self):
        self._complete_level(8, check_algorithm_score=False)

    def test_level_009(self):
        self._complete_level(9, check_algorithm_score=False)

    def test_level_010(self):
        self._complete_level(10, check_algorithm_score=False)

    def test_level_011(self):
        self._complete_level(11, check_algorithm_score=False)

    def test_level_012(self):
        self._complete_level(12, check_algorithm_score=False)

    def test_episode_02(self):
        self._complete_episode(2, 13)

    def test_level_013(self):
        self._complete_level(13)

    def test_level_014(self):
        self._complete_level(14)

    def test_level_015(self):
        self._complete_level(15)

    def test_level_016(self):
        self._complete_level(16)

    def test_level_017(self):
        self._complete_level(17)

    def test_level_018(self):
        self._complete_level(18)

    def test_episode_03(self):
        self._complete_episode(3, 19)

    def test_level_019(self):
        self._complete_level(19)

    def test_level_020(self):
        self._complete_level(20)

    def test_level_021(self):
        self._complete_level(21)

    def test_level_022(self):
        self._complete_level(22)

    def test_level_023(self):
        self._complete_level(23)

    def test_level_024(self):
        self._complete_level(24)

    def test_level_025(self):
        self._complete_level(25)

    def test_level_026(self):
        self._complete_level(26)

    def test_level_027(self):
        self._complete_level(27)

    def test_level_028(self):
        self._complete_level(28)

    def test_episode_04(self):
        self._complete_episode(4, 29)

    def test_level_029(self):
        self._complete_level(29)

    def test_level_030(self):
        self._complete_level(30)

    def test_level_031(self):
        self._complete_level(31)

    def test_level_032(self):
        self._complete_level(32)

    def test_episode_05(self):
        self._complete_episode(5, 33)

    def test_level_033(self):
        self._complete_level(33)

    def test_level_034(self):
        self._complete_level(34)

    def test_level_035(self):
        self._complete_level(35)

    def test_level_036(self):
        self._complete_level(36)

    def test_level_037(self):
        self._complete_level(37)

    def test_level_038(self):
        self._complete_level(38)

    def test_level_039(self):
        self._complete_level(39, check_route_score=False)

    def test_level_040(self):
        self._complete_level(40)

    def test_level_041(self):
        self._complete_level(41)

    def test_level_042(self):
        self._complete_level(42)

    def test_level_043(self):
        self._complete_level(43)

    def test_episode_06(self):
        self._complete_episode(6, 44)

    def test_level_044(self):
        self._complete_level(44)

    def test_level_045(self):
        self._complete_level(45)

    def test_level_046(self):
        self._complete_level(46)

    def test_level_047(self):
        self._complete_level(47)

    def test_level_048(self):
        self._complete_level(48)

    def test_level_049(self):
        self._complete_level(49)

    def test_level_050(self):
        self._complete_level(50)

    def test_episode_07(self):
        self._complete_episode(7, 51, check_algorithm_score=False)

    def test_level_051(self):
        self._complete_level(51, check_algorithm_score=False)

    def test_level_052(self):
        self._complete_level(52, check_route_score=False)

    def test_level_053(self):
        self._complete_level(53)

    def test_level_054(self):
        self._complete_level(54, check_route_score=False)

    def test_level_055(self):
        self._complete_level(55)

    def test_level_056(self):
        self._complete_level(56)

    def test_level_057(self):
        self._complete_level(57)

    def test_level_058(self):
        self._complete_level(58)

    def test_level_059(self):
        self._complete_level(59, check_route_score=False)

    def test_level_060(self):
        self._complete_level(60, check_route_score=False)

    def test_episode_08(self):
        self._complete_episode(8, 61)

    def test_level_061(self):
        self._complete_level(61)

    def test_level_062(self):
        self._complete_level(62)

    def test_level_063(self):
        self._complete_level(63)

    def test_level_064(self):
        self._complete_level(64)

    def test_level_065(self):
        self._complete_level(65)

    def test_level_066(self):
        self._complete_level(66)

    def test_level_067(self):
        self._complete_level(67)

    def test_episode_09(self):
        self._complete_episode(9, 68, check_route_score=False)

    def test_level_068(self):
        self._complete_level(68, check_route_score=False)

    def test_level_069(self):
        self._complete_level(69, check_route_score=False)

    def test_level_070(self):
        self._complete_level(70, check_route_score=False)

    def test_level_071(self):
        self._complete_level(71)

    def test_level_072(self):
        self._complete_level(72)

    def test_level_073(self):
        self._complete_level(73)

    def test_level_074(self):
        self._complete_level(74, check_route_score=False)

    def test_level_075(self):
        self._complete_level(75)

    def test_level_076(self):
        self._complete_level(76, check_route_score=False)

    def test_level_077(self):
        self._complete_level(77, check_route_score=False)

    def test_level_078(self):
        self._complete_level(78, check_route_score=False)

    def test_level_079(self):
        self._complete_level(79, final_level=True)

    def test_episode_12(self):
        self._complete_episode(
            12, 1, check_algorithm_score=False, from_python_den=True
        )

    def test_python_level_001(self):
        self._complete_level(1, from_python_den=True)

    def test_python_level_002(self):
        self._complete_level(2, from_python_den=True)

    def test_python_level_003(self):
        self._complete_level(3, from_python_den=True)

    def test_python_level_004(self):
        self._complete_level(
            4, check_algorithm_score=False, from_python_den=True
        )

    def test_python_level_005(self):
        self._complete_level(
            5, check_algorithm_score=False, from_python_den=True
        )

    def test_python_level_006(self):
        self._complete_level(
            6, check_algorithm_score=False, from_python_den=True
        )

    def test_python_level_007(self):
        self._complete_level(7, from_python_den=True)

    def test_python_level_008(self):
        self._complete_level(8, from_python_den=True)

    def test_python_level_009(self):
        self._complete_level(9, from_python_den=True)

    def test_python_level_010(self):
        self._complete_level(
            10, check_algorithm_score=False, from_python_den=True
        )

    def test_python_level_011(self):
        self._complete_level(
            11, check_algorithm_score=False, from_python_den=True
        )

    def test_python_level_012(self):
        self._complete_level(
            12, check_algorithm_score=False, from_python_den=True
        )

    def test_python_level_013(self):
        self._complete_level(
            13, check_algorithm_score=False, from_python_den=True
        )

    def test_episode_13(self):
        self._complete_episode(13, 14, from_python_den=True)

    def test_python_level_014(self):
        self._complete_level(14, from_python_den=True)

    def test_python_level_015(self):
        self._complete_level(15, from_python_den=True)

    def test_python_level_016(self):
        self._complete_level(
            16, check_algorithm_score=False, from_python_den=True
        )

    def test_python_level_017(self):
        self._complete_level(
            17, check_algorithm_score=False, from_python_den=True
        )

    def test_python_level_018(self):
        self._complete_level(
            18, check_algorithm_score=False, from_python_den=True
        )

    def test_python_level_019(self):
        self._complete_level(19, from_python_den=True)

    def test_python_level_020(self):
        self._complete_level(
            20, check_algorithm_score=False, from_python_den=True
        )

    def test_python_level_021(self):
        self._complete_level(
            21, check_algorithm_score=False, from_python_den=True
        )

    def test_python_level_022(self):
        self._complete_level(22, from_python_den=True)

    def test_python_level_023(self):
        self._complete_level(23, from_python_den=True)

    def test_python_level_024(self):
        self._complete_level(
            24, check_algorithm_score=False, from_python_den=True
        )

    def test_python_level_025(self):
        self._complete_level(
            25, check_algorithm_score=False, from_python_den=True
        )

    def test_episode_14(self):
        self._complete_episode(14, 26, from_python_den=True)

    def test_python_level_026(self):
        self._complete_level(26, from_python_den=True)

    def test_python_level_027(self):
        self._complete_level(27, from_python_den=True)

    def test_python_level_028(self):
        self._complete_level(28, from_python_den=True)

    def test_python_level_029(self):
        self._complete_level(29, from_python_den=True)

    def test_python_level_030(self):
        self._complete_level(
            30, check_algorithm_score=False, from_python_den=True
        )

    def test_python_level_031(self):
        self._complete_level(31, from_python_den=True)

    def test_python_level_032(self):
        self._complete_level(32, from_python_den=True)

    def test_python_level_033(self):
        self._complete_level(
            33, check_algorithm_score=False, from_python_den=True
        )

    def test_python_level_034(self):
        self._complete_level(
            34, check_algorithm_score=False, from_python_den=True
        )

    def test_python_level_035(self):
        self._complete_level(35, from_python_den=True)

    def test_python_level_036(self):
        self._complete_level(36, from_python_den=True)

    def test_python_level_037(self):
        self._complete_level(
            37, check_algorithm_score=False, from_python_den=True
        )

    @pytest.mark.skip(reason="this level's solution is currently flawed")
    def test_python_level_038(self):
        self._complete_level(
            38, check_algorithm_score=False, from_python_den=True
        )

    def test_python_level_039(self):
        self._complete_level(
            39, check_algorithm_score=False, from_python_den=True
        )

    def test_python_level_040(self):
        self._complete_level(
            40,
            check_algorithm_score=False,
            from_python_den=True,
            redirects=True,
        )

    def test_episode_15(self):
        self._complete_episode(
            15, 41, check_algorithm_score=False, from_python_den=True
        )

    def test_python_level_041(self):
        self._complete_level(41, from_python_den=True)

    def test_python_level_042(self):
        self._complete_level(
            42, check_algorithm_score=False, from_python_den=True
        )

    def test_python_level_043(self):
        self._complete_level(
            43, check_algorithm_score=False, from_python_den=True
        )

    def test_python_level_044(self):
        self._complete_level(44, from_python_den=True)

    def test_python_level_045(self):
        self._complete_level(
            45, check_algorithm_score=False, from_python_den=True
        )

    def test_python_level_046(self):
        self._complete_level(
            46, check_algorithm_score=False, from_python_den=True
        )

    def test_python_level_047(self):
        self._complete_level(
            47, check_algorithm_score=False, from_python_den=True
        )

    def test_python_level_048(self):
        self._complete_level(
            48, check_algorithm_score=False, from_python_den=True
        )

    def test_python_level_049(self):
        self._complete_level(
            49,
            check_algorithm_score=False,
            from_python_den=True,
            final_level=True,
        )
