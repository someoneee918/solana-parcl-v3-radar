#!/usr/bin/env python3
"""
Unit Tests for Solana Parcl v3 Real Estate Synthetics Radar
"""

import unittest
from parcl_v3_radar import (
    calculate_market_skew_impact,
    calculate_parcl_liquidation_boundary,
    calculate_liquidator_reward,
    calculate_lp_yield_and_delta,
    generate_vip_sentinel_script,
    SOL_RECEIVE_ADDRESS,
    BASE_RECEIVE_ADDRESS
)

class TestParclV3Radar(unittest.TestCase):

    def test_market_skew_impact(self):
        # Long OI $3M, Short OI $1M, Pool $5M. Base rate 5.0%
        # Net skew: +$2M. Skew ratio: 2M / 5M = 40% (0.40)
        # Utilization: 4M / 5M = 80%
        # Dynamic skew rate: 0.40 * 0.20 = 0.08 (8.0%)
        # Long borrow APR: 5% + 8% = 13.0%. Short borrow: 5.0%
        res = calculate_market_skew_impact(
            long_oi_usd=3000000.0,
            short_oi_usd=1000000.0,
            pool_liquidity_usd=5000000.0,
            base_borrow_rate_annual=0.05
        )
        self.assertEqual(res["net_skew_usd"], 2000000.0)
        self.assertEqual(res["pool_utilization_pct"], 80.0)
        self.assertEqual(res["skew_ratio_pct"], 40.0)
        self.assertEqual(res["dominant_side"], "LONGS_DOMINANT")
        self.assertEqual(res["long_borrow_apr_pct"], 13.0)
        self.assertEqual(res["short_borrow_apr_pct"], 5.0)

    def test_parcl_liquidation_boundary(self):
        # NYC City Index @ $2,500. 10x Long. Maintenance margin 5.0% (0.05)
        # Reciprocal = 1 / 10 = 0.10.
        # Liq price = 2500 * (1 - 0.10 + 0.05) = 2500 * 0.95 = $2,375.00 (5.0% drop)
        long_pos = calculate_parcl_liquidation_boundary(
            entry_price=2500.0,
            leverage=10.0,
            is_long=True,
            maint_margin_pct=0.05
        )
        self.assertEqual(long_pos["liquidation_price"], 2375.0)
        self.assertEqual(long_pos["distance_to_liq_pct"], 5.0)
        
        # 10x Short @ $2,500.
        # Liq price = 2500 * (1 + 0.10 - 0.05) = 2500 * 1.05 = $2,625.00 (5.0% rise)
        short_pos = calculate_parcl_liquidation_boundary(
            entry_price=2500.0,
            leverage=10.0,
            is_long=False,
            maint_margin_pct=0.05
        )
        self.assertEqual(short_pos["liquidation_price"], 2625.0)
        self.assertEqual(short_pos["distance_to_liq_pct"], 5.0)

    def test_liquidator_reward(self):
        # Position: $20,000. Bonus: 2.5% = $500.00. Jito tip: $0.05 -> Net: $499.95.
        reward = calculate_liquidator_reward(
            position_size_usd=20000.0,
            liquidator_bonus_pct=0.025,
            jito_tip_usd=0.05,
            sol_price_usd=140.0
        )
        self.assertEqual(reward["gross_reward_usd"], 500.0)
        self.assertEqual(reward["net_reward_usd"], 499.95)
        self.assertTrue(reward["is_profitable"])
        self.assertAlmostEqual(reward["net_reward_sol"], 499.95 / 140.0, places=4)

    def test_lp_yield_and_delta(self):
        # Pool: $10,000,000. Volume: $2,000,000/day. Fee: 0.20% (0.002).
        # Daily fees = $2M * 0.002 = $4,000. Annual: $1,460,000. Fee APY: 14.6%.
        # Net skew: +$1,500,000 longs -> LP Delta: -$1,500,000 (short bias).
        res = calculate_lp_yield_and_delta(
            pool_liquidity_usd=10000000.0,
            daily_volume_usd=2000000.0,
            net_skew_usd=1500000.0,
            trading_fee_pct=0.002
        )
        self.assertEqual(res["daily_fees_usd"], 4000.0)
        self.assertEqual(res["annual_fees_usd"], 1460000.0)
        self.assertEqual(res["fee_apy_pct"], 14.6)
        self.assertEqual(res["lp_delta_exposure_usd"], -1500000.0)

    def test_generate_vip_script(self):
        script = generate_vip_sentinel_script(SOL_RECEIVE_ADDRESS, BASE_RECEIVE_ADDRESS)
        self.assertIn("Parcl Sentinel", script)
        self.assertIn(SOL_RECEIVE_ADDRESS, script)
        self.assertIn(BASE_RECEIVE_ADDRESS, script)
        self.assertIn("@parcl-oss/v3-sdk", script)

if __name__ == "__main__":
    unittest.main()
