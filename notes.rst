=======
Outline
=======

Title: Object oriented implementation of Yeadon's human inertial model

Introduction
============

- What human inertia calcs are
- Why you need them
- How people use them
- How they obtain
- Review of existing software
- Winter text book on biomechanics (compare height and mass)
- Intro to Yeadon's model and citations to him.
- Why we use Yeadon's model.
  ** CHRIS: goal is also to clear up some of the implementation details of the method, that are not clear from the paper alone. therefore promoting consistent use of the method

Find papers that use this model:
- Alison Sheet's work
- compare to her matlab code

Yeadon's Method
---------------

Brief explanation
FIGURE - measurements
FIGURE - cfg

Since not all levels "lengths" are not measured, etc, we average some, the corresponding perimeter must be measured at the correct mid-arm point, etc.

There are x segments: (1).. (2) , (3)... say how many solids thye have each.

There are x degrees of freedom: (1), (2)...etc.

There are segments, composed of solids lofted between parallel stadia.

Location of hip joint centres with respect to pelvis: unspecified in yeadon papers?

segments are rigid bodies, composed of solids.

see comment in yeadon-ii about trapezium when t = 0

solids comprising a segment have coincident longitudinal axis.

we also use dempster's densities.

intended purpose was aerial movementSs: twisting somersalts on a trampoline.

Software Design
===============

- Utility
- proven advantage
- long term advantage
- mainenance and potential for growth
- algorithms
- object model (pylint may generate UML diagrams)
- modularity
- open source
- how does this software make it easy to integrate with anaylysis
- software license

Validation - chris
==========

- demonstrate that it achvies purpose
- prove improvement over existing
- proof of principle example
- Jason will look at diss but for now compare to Yeadon's code.
- Show comparison numeric tables.
- test data
- direct link

How to install the software
===========================

cross platform

How to use the software - chris
=======================
- Command line
- UI
- ??GUI!!
- show basic usage then a bigger example
- FIGURE spinning ice skater example
- input file format description
- code snippets

Example
=======

- (Results)
- Person sitting on bicycle.
- Reference the software where this is implemented.
- Show numerical numbers of benchamrk bicycle and then the examples after
- can we show something that goes beyond just calculating the numbers and the images?
- compare easy of generating inertia for different models (rigid rider vs multisegment rider)
- FIGURE 

crtl-v, select rows, ctrl-i to insert on each row, esc

Given measurements
------------------
talk about how the data for female1, male1, etc. was gathered.


notes on measurementS:
-reorder PTC to CTP
-change lineweights or move labels of P T C on the actual guy
- or make a note about what the colors mean

Style
-----
Chris: I try to type numbers out as numerals rather than as words whenever possible; I think it's easier to read. However, I understand it's conventional to write out small numbers so I'm fine with us doing that.

we vs passive
