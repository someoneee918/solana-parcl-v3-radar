# Solana Parcl v3 Real Estate Synthetics & Risk Radar

[![Python Unit Tests](https://img.shields.io/badge/Unit%20Tests-5%2F5%20Passing-brightgreen.svg)]()
[![Solana](https://img.shields.io/badge/Solana-Mainnet--Beta-blueviolet.svg)]()
[![Parcl v3](https://img.shields.io/badge/Protocol-Parcl%20v3-cyan.svg)]()
[![Live Visualizer](https://img.shields.io/badge/Live%20Dashboard-GitHub%20Pages-blue.svg)](https://someoneee918.github.io/solana-parcl-v3-radar/)

Commercial DeFi intelligence engine analyzing:
1. **City Index Synthetics (NYC, Miami, London) Long vs Short Open Interest Skew on Solana**
2. **Parcl v3 Dynamic Price Impact & Skew-Weighted Borrow Carry Drag**
3. **10x Leverage Maintenance Margin (MMR 5.0%) Exact Liquidation Boundaries**
4. **Single-LP Tranche Delta Exposure & Real Estate Fee Yield Economics**
5. **Non-Custodial VIP Sentinel License Generator (5 Base USDC / 0.03 SOL)**

---

## Live Interactive Dashboard
🌐 **Access the live dashboard at**: [https://someoneee918.github.io/solana-parcl-v3-radar/](https://someoneee918.github.io/solana-parcl-v3-radar/)

---

## Key Mathematical Models

### 1. Parcl City Index Open Interest Skew
$$\text{Skew}_{ratio} = \frac{\text{Long OI} - \text{Short OI}}{\text{Pool Liquidity}}$$
$$\text{Borrow APR}_{long} = R_{base} + \max(0, \text{Skew}_{ratio} \times 0.20)$$

When real estate traders lean heavily long on NYC or Miami, long borrow financing rates scale proportionally to incentivize balanced inventory.

### 2. 10x Leverage Liquidation Boundary Precision
For maximum leverage $L = 10.0\text{x}$ and maintenance margin $MMR = 5.0\%$:
$$P_{liq} = P_{entry} \times \left(1 - \frac{1}{L} + MMR\right)$$

For $P_{entry} = \$2,500.00\text{ USD}$:
$$P_{liq} = \$2,500.00 \times (1 - 0.10 + 0.05) = \$2,375.00\text{ USD}$$
- Liquidation triggers on a **$5.00\%$ adverse move**.

---

## Unit Test Verification
Run the 5/5 unit test suite:
```bash
python3 -m unittest test_parcl_v3_radar.py
```

---

## Non-Custodial VIP Sentinel License
Unlock automated TypeScript `@parcl-oss/v3-sdk` real estate index position guardian and Jito liquidation bot scripts by sending **5 Base USDC** or **0.03 SOL** to our verified receive addresses:
- **Solana:** `DW2MdHEq3qZ6nh9b5YFUoaPnBuuxC8Gz2785kwbbjSAM`
- **Base EVM:** `0xF0E0D361bBE899F3089f0a968506eF2B97693c01`
