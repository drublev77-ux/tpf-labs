---
title: "Blueberry picking robot: how selective harvesting works, and when it pays"
seo_title: "Blueberry picking robot: how it works, what it costs"
description: "How a blueberry picking robot finds, grips and grades ripe berries, what it means for crew size and cost per kilogram, and how to test one on your farm."
date: 2026-11-03
lang: en
slug: blueberry-picking-robot-how-it-works
cluster: machines
---

# Blueberry picking robot: how selective harvesting works, and when it pays

A blueberry picking robot does what a picking crew does, berry by berry. A shaker harvester does something else: it takes the whole bush at once. That difference sets the rest of the economics. The robot keeps fresh-market grade but has to be fast enough to replace hands. The shaker is fast but turns premium fruit into processing fruit. This guide explains how a selective robot works, where the limits are and how to decide if one belongs on your farm.

## What a blueberry picking robot actually does

Every selective robot repeats the same four steps for each berry, thousands of times an hour:

1. **See.** Cameras scan the bush from several angles. A vision model separates ripe berries from green, red and damaged ones, including berries half hidden behind leaves.
2. **Decide.** The software chooses which berries to pick on this pass and in what order, so the arms do not cross or knock fruit off the branch.
3. **Pick.** An arm moves to the berry and a soft gripper detaches it with a gentle twist or pull, the way a picker's fingers do.
4. **Place.** The berry goes into a padded, cooled container instead of falling through a catch frame.

Ripeness is the hard part. A blueberry changes from red to blue in days, and the bloom (the white wax on the skin) is one of the things buyers check. A robot that rubs the bloom off or picks reddish berries fails the fresh market even if it is fast.

## How CALIBER+ is built

CALIBER+ is the selective harvester we are developing at TPF Labs. Its design targets show the main choices behind a picking robot:

- **Two rows at once.** The machine straddles the row. Two manipulators per side work from vertical carriages, so one pass covers both sides of two bush lines.
- **SCARA arms.** SCARA arms are fast and precise in the horizontal plane, which matches how berries hang on a bush. The vertical carriage handles height.
- **AI ripeness vision.** A detection model trained on a 50,000-image berry dataset finds ripe berries and skips green ones, pass after pass.
- **Soft hybrid gripper.** Silicone fingers with vacuum assist hold each berry with under 2 N of force, to keep the skin and bloom intact.
- **Chilled hopper.** A 60 L cooled container slows the loss of quality between the bush and the packhouse.
- **Hot-swap battery.** The design target is 12–14 hours of work a day, and a battery swap takes under a minute.

These are design targets for a machine in pre-production, not results from a commercial fleet. Pilot farms will measure them on their own rows in 2027.

## Robot vs crew vs shaker: what changes on the farm

| | Picking crew | Shaker harvester | Selective picking robot |
|---|---|---|---|
| Fruit quality | Fresh market | Mostly processing | Fresh market (design goal) |
| Ripeness | Pickers choose | Ripe and green mixed | Ripe only, berry by berry |
| People needed | A full crew | Driver plus sorting | One operator per machine |
| Cost driver | Wages, housing, transport | Machine price, fuel, losses | Season fee or purchase |
| Main risk | Finding people on time | Downgraded fruit | New technology |

A robot does not remove people from the farm. It changes the job: fewer people picking, and some people running machines, checking quality and handling fruit.

## When a picking robot pays off

A robot pays off when three conditions meet:

- **You sell fresh-market fruit.** If your berries go to processing, a shaker is cheaper per kilogram and the robot's gentle handling earns nothing extra.
- **Labour is your bottleneck.** If you lose fruit or grade because the crew arrives late or is too small, every hour a machine works in the peak is worth more than its average cost.
- **The numbers per kilogram work.** Manual picking costs about €2.4 per kilogram. A CALIBER+ season contract (Robot-as-a-Service) is €26,000 per season with service and software included, about €1.9 per kilogram of picked berries. Purchase starts at €80,000.

On 100 tonnes of fresh-market berries that is roughly €240,000 for manual picking against about €190,000 with RaaS. Our [cost per kilogram guide](/blog/en/blueberry-harvesting-machine-cost-2026/) walks through that example in detail.

## What to ask any robot supplier

1. **Measured, not promised.** Ask for kilograms per hour, loss rate and share of unripe fruit picked, measured on a farm like yours.
2. **Your varieties and trellis.** Bush shape, row spacing and variety change everything. Ask how the vision model is recalibrated for your plants.
3. **Service in the peak.** Ask how fast a technician reaches the field in harvest week, and who pays for downtime.
4. **Who owns the data.** Ripeness maps and yield per row are valuable. Make sure you get them.
5. **How to exit.** A good offer lets you test before you commit. See [how a machine compares with the other options](/blog/en/blueberry-harvesting-machine-types-costs/).

## How to test a picking robot on your own rows

The CALIBER+ pilot runs 30/60/90 days. First a row survey and vision calibration for your varieties. Then autonomous harvesting on one hectare, measuring ripeness, calibre, losses and cost per kilogram. At the end you get a full report and the option to lock a tariff or buy for the next season. There is no financial obligation until you sign a season contract.

Pilot slots for season 2027 are open. Write to [orders@tpf-technology.com](mailto:orders@tpf-technology.com) with your acreage, varieties and harvest window, or read more on the [CALIBER+ page](/).

## FAQ

**Can a robot really pick blueberries without damaging them?**
That is the main design challenge. CALIBER+ uses a soft silicone gripper with vacuum assist and a target grip force under 2 N, so the skin and bloom stay intact. Pilot farms will measure damage rates on their own fruit in 2027.

**How fast is a blueberry picking robot?**
Speed depends on the machine, the bush and the yield. The CALIBER+ design target is 17 kg per hour per machine, over 12–14 hours of work a day.

**Will a picking robot replace my whole crew?**
No. It reduces how many people you need for picking at peak. You still need people to run the machines, check quality and handle fruit in the packhouse.

**How much does a blueberry picking robot cost?**
A CALIBER+ season contract is €26,000 per season including service and updates, about €1.9 per kilogram. Purchase starts at €80,000.
