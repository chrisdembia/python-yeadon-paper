Dear Arnaud Barré,

Thank you very much for lending your time and expertise for this review. We are
happy that you have approved the article and appreciate your thorough review.
We have submitted a second revision to address your comments and suggestions.
The responses for each of your comments follow:

   However, it would be interesting to have a better comparison of the
   different methods proposed to compute body segment inertial parameters using
   direct and indirect methods. For example, the authors mentions the facility
   of Yeadon's method compared to other studies, but the number of measurements
   is large compared to others studies not cited, like de Leva (1996) or Dumas
   et al. (2007). These indirect methods have also error as explained in Rossi
   et al. (2013). What is the advantage of Yeadon's method compared to others?
   A discussion on the limitations of the model proposed (joint center
   accuracy, joint range, mass estimation, density scaling, etc.) would be also
   of interest.

We also think that a paper showing the disadvantages and advantages of these
various models would be very beneficial but we believe that this undertaking is
out of the scope of this paper. We are leaving these discussions to other
literature and would like to keep the scope of this paper about the specific
software implementation of one method that has been described, judged, and
commented on elsewhere. If the reviewer would like to work on this idea with us
for a future publication we could certainly discuss possibilities.

   The authors modified some parts of the original model, why did they not add
   joint centers for ankles and wrists? This would give a better general
   behavior to the avatar.

We aimed to create a faithful representation of Yeadon's model and thus did not
include extra joints. But the object oriented nature of our software design
would allow relatively easy sub-classing to implement other models with more
joints.

Another reason we did not worry much about the ankle and wrist joints was due
to our intended application: whole body inertia of a bicycle rider. The
inertial difference in a whole body model with and without ankle and wrist
joints is very small, in our case negligible. It is only important when one is
worried about those specific segments of the body. Yeadon's model is likely not
suitable for models that focus on the hand or foot. It was not necessarily
designed to predict the body segment parameters on a individual basis but to
predict whole body inertia, and this is how we use the model.

The text has been updated to reflect this, see:

https://github.com/chrisdembia/python-yeadon-paper/pull/63

   Figure 1: The authors should give the abbreviations of the body parts. It is
   not obvious why all the levels for the torso does not use the P,T,C letters,
   but 's' instead. I understand this is the original nomenclature used by M.R.
   Yeadon, but this should be detailed. Moreover, as explained later in the
   manuscript, some segments have two levels at the same location (for example,
   shoulder and neck levels are abbreviated by Ls5), they would be
   distinguished for clarity. Thus, this would help to better understand the
   departures proposed (like in Acromion stadia).

We clarified more on the P, T, C letters here:

https://github.com/chrisdembia/python-yeadon-paper/pull/64

But we felt that we adequately addressed the single level that shares two
different sized stadia and that further improvement with, for example, more
subscripts would be overkill.

   Figure 1: In the legend "segments, label, solids", the segment A2 is defined
   between a2 and s6. I assume it is a6 and not s6.

Keen eye!, fixed here:

https://github.com/chrisdembia/python-yeadon-paper/pull/52

   "Measurements": fifth paragraph: The authors should mention the potential
   accuracy issue related to the scaling of the densities (homogeneous scaling
   over the body, possibly increasing the error with the body segment inertial
   parameters). This could be in the discussion.

We agree that there are potential accuracy issues with scaling the densities by
mass, but we also believe that this is a logical thing to do and that it more
than likely reduces error in the inertial estimates. We've added a sentence to
warn the user that there can be pitfalls:

https://github.com/chrisdembia/python-yeadon-paper/pull/59

   "Configuration" paragraph 1: The authors wrote "somersalt" instead of
   "somersault". (Also in page 7).

Fixed here: https://github.com/chrisdembia/python-yeadon-paper/pull/51

   Formulas 1 and 2: These formulas give only the x coordinates of the hip
   center joint. What about the y and z coordinates?

We've clarified how the origin of the model is defined and thus the y and z
coordinates are zero by definition.

Fixed here: https://github.com/chrisdembia/python-yeadon-paper/pull/58

   Formulas 3, 4, 5: The authors should use a suffix to the computed parameters
   to clarify the associated level.

Fixed here: https://github.com/chrisdembia/python-yeadon-paper/pull/57

   "Relationships between configuration variables": The authors wrote "21
   configuration variables;". Please modify to "21 joint angle configuration
   variables to clarify".

Fixed here: https://github.com/chrisdembia/python-yeadon-paper/pull/55

   "Degenerate Stadia": What are the manipulations? Please detail.

Fixed here: https://github.com/chrisdembia/python-yeadon-paper/pull/66

   "Software design": Please add a reference for "Python" as this is the only
   one tool that does not have one (compared to Mayavi or VTK). The authors
   should also indicate that the library is implemented with Python 2.7. Their
   code could not be compatible with Python 3.

Thanks, it is good to note the Python 3 incompatibility. We are unfortunately
tied to the Mayavi/VTK tool chain which does not yet support Python 3.

Fixed here: https://github.com/chrisdembia/python-yeadon-paper/pull/54

   Figure 5: How did the authors fix the joint angular range? This seems to be
   empirical but it should be at least mentioned in the manuscript.

Fixed here: https://github.com/chrisdembia/python-yeadon-paper/pull/62

Sincerely,

Chris Dembia, Jason K. Moore, and Mont Hubbard
