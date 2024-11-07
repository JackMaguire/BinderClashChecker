CONFLICT `<class 'pyrosetta.rosetta.protocols.symmetry.SequentialSymmetrySlider'>` 
 - `[<class 'pyrosetta.rosetta.protocols.symmetry.SymmetrySlider'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.symmetry.SequentialSymmetrySlider'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.symmetry.RandomSymmetrySlider'>` 
 - `[<class 'pyrosetta.rosetta.protocols.symmetry.SymmetrySlider'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.symmetry.RandomSymmetrySlider'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.simple_moves.ClassicFragmentMover'>` 
 - `[<class 'pyrosetta.rosetta.core.fragment.FragSet'>, <class 'pyrosetta.rosetta.core.kinematics.MoveMap'>]` 
 - `[<class 'pyrosetta.rosetta.core.fragment.ConstantLengthFragSet'>, <class 'pyrosetta.rosetta.core.kinematics.MoveMap'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.simple_moves.ChangeAndResetFoldTreeMover'>` 
 - `[<class 'pyrosetta.rosetta.protocols.moves.Mover'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.simple_moves.ChangeAndResetFoldTreeMover'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.simple_filters.StructuralSimilarityEvaluator'>::assign` 
 - `[<class 'pyrosetta.rosetta.protocols.evaluation.SingleValuePoseEvaluator_double_t'>, <class 'pyrosetta.rosetta.protocols.evaluation.SingleValuePoseEvaluator_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.evaluation.SingleValuePoseEvaluator_double_t'>, <class 'pyrosetta.rosetta.protocols.evaluation.PoseEvaluator'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.simple_filters.JScoreEvaluator'>::assign` 
 - `[<class 'pyrosetta.rosetta.protocols.evaluation.SingleValuePoseEvaluator_double_t'>, <class 'pyrosetta.rosetta.protocols.evaluation.SingleValuePoseEvaluator_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.evaluation.SingleValuePoseEvaluator_double_t'>, <class 'pyrosetta.rosetta.protocols.evaluation.PoseEvaluator'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.simple_filters.ContactMapEvaluator'>::assign` 
 - `[<class 'pyrosetta.rosetta.protocols.evaluation.SingleValuePoseEvaluator_double_t'>, <class 'pyrosetta.rosetta.protocols.evaluation.SingleValuePoseEvaluator_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.evaluation.SingleValuePoseEvaluator_double_t'>, <class 'pyrosetta.rosetta.protocols.evaluation.PoseEvaluator'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.residue_selectors.NativeSelector'>` 
 - `[<class 'pyrosetta.rosetta.core.select.residue_selector.ResidueSelector'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.residue_selectors.NativeSelector'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.pockets.TargetPocketGrid'>` 
 - `[<class 'pyrosetta.rosetta.protocols.pockets.PocketGrid'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.pockets.TargetPocketGrid'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.pockets.EggshellGrid'>` 
 - `[<class 'pyrosetta.rosetta.protocols.pockets.PocketGrid'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.pockets.EggshellGrid'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.pack_daemon.LnExpression'>` 
 - `[<class 'pyrosetta.rosetta.numeric.expression_parser.Expression'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.pack_daemon.LnExpression'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.pack_daemon.InSetExpression'>` 
 - `[<class 'pyrosetta.rosetta.numeric.expression_parser.Expression'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.pack_daemon.InSetExpression'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.pack_daemon.ExpExpression'>` 
 - `[<class 'pyrosetta.rosetta.numeric.expression_parser.Expression'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.pack_daemon.ExpExpression'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.multistate_design.PosType'>::assign` 
 - `[<class 'pyrosetta.rosetta.protocols.multistate_design.PosType'>, <class 'pyrosetta.rosetta.protocols.multistate_design.PosType'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.multistate_design.PosType'>, <class 'pyrosetta.rosetta.protocols.genetic_algorithm.EntityElement'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.multistage_rosetta_scripts.cluster.metrics.SequenceMetric'>::distance` 
 - `[<class 'pyrosetta.rosetta.protocols.multistage_rosetta_scripts.cluster.metrics.SequenceMetric'>, <class 'pyrosetta.rosetta.protocols.multistage_rosetta_scripts.cluster.metrics.SequenceMetric'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.multistage_rosetta_scripts.cluster.metrics.SequenceMetric'>, <class 'pyrosetta.rosetta.protocols.multistage_rosetta_scripts.cluster.ClusterMetric'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.multistage_rosetta_scripts.cluster.metrics.JumpMetric'>::distance` 
 - `[<class 'pyrosetta.rosetta.protocols.multistage_rosetta_scripts.cluster.metrics.JumpMetric'>, <class 'pyrosetta.rosetta.protocols.multistage_rosetta_scripts.cluster.metrics.JumpMetric'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.multistage_rosetta_scripts.cluster.metrics.JumpMetric'>, <class 'pyrosetta.rosetta.protocols.multistage_rosetta_scripts.cluster.ClusterMetric'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.RotMatrix'>::swap` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>, <class 'pyrosetta.rosetta.std.vector_utility_vector1_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>, <class 'pyrosetta.rosetta.std.vector_utility_vector1_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.RotMatrix'>::size` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.RotMatrix'>::resize` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>, <class 'int'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>, <class 'int'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.RotMatrix'>::reserve` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>, <class 'int'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>, <class 'int'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.RotMatrix'>::pop_back` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.RotMatrix'>::max_size` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.RotMatrix'>::empty` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.RotMatrix'>::clear` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.RotMatrix'>::capacity` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>::swap` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>, <class 'pyrosetta.rosetta.std.vector_utility_vector1_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>, <class 'pyrosetta.rosetta.std.vector_utility_vector1_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>::size` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>::resize` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>, <class 'int'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>, <class 'int'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>::reserve` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>, <class 'int'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>, <class 'int'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>::pop_back` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>::max_size` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>::empty` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>::clear` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>::capacity` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>, <class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>, <class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>, <class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>, <class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_RotProb_std_allocator_protocols_mean_field_RotProb_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>::swap` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>, <class 'pyrosetta.rosetta.std.vector_utility_vector1_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>, <class 'pyrosetta.rosetta.std.vector_utility_vector1_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>::size` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>::resize` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>, <class 'int'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>, <class 'int'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>::reserve` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>, <class 'int'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>, <class 'int'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>::pop_back` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>::max_size` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>::empty` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>::clear` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>::capacity` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>, <class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>, <class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>, <class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>, <class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>::swap` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>, <class 'pyrosetta.rosetta.std.vector_utility_vector1_double_std_allocator_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_double_std_allocator_double_t'>, <class 'pyrosetta.rosetta.std.vector_utility_vector1_double_std_allocator_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>::size` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_double_std_allocator_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>::resize` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>, <class 'int'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_double_std_allocator_double_t'>, <class 'int'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>::resize` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>, <class 'int'>, <class 'pyrosetta.rosetta.utility.vector1_double'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_double_std_allocator_double_t'>, <class 'int'>, <class 'pyrosetta.rosetta.utility.vector1_double'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>::reserve` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>, <class 'int'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_double_std_allocator_double_t'>, <class 'int'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>::push_back` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>, <class 'pyrosetta.rosetta.utility.vector1_double'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_double_std_allocator_double_t'>, <class 'pyrosetta.rosetta.utility.vector1_double'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>::pop_back` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_double_std_allocator_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>::max_size` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_double_std_allocator_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>::front` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_double_std_allocator_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>::empty` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_double_std_allocator_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>::clear` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_double_std_allocator_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_double_std_allocator_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>::capacity` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_double_std_allocator_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>::back` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_double_std_allocator_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>::at` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>, <class 'int'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_double_std_allocator_double_t'>, <class 'int'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>, <class 'pyrosetta.rosetta.utility.vector1_utility_vector1_double_std_allocator_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>, <class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>, <class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>, <class 'pyrosetta.rosetta.utility.vector1_utility_vector1_double_std_allocator_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_double_std_allocator_double_t'>, <class 'int'>, <class 'pyrosetta.rosetta.utility.vector1_double'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_double_std_allocator_double_t'>, <class 'int'>, <class 'pyrosetta.rosetta.utility.vector1_double'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.AAMatrix'>::swap` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>, <class 'pyrosetta.rosetta.std.vector_utility_vector1_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>, <class 'pyrosetta.rosetta.std.vector_utility_vector1_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.AAMatrix'>::size` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.AAMatrix'>::resize` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>, <class 'int'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>, <class 'int'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.AAMatrix'>::reserve` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>, <class 'int'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>, <class 'int'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.AAMatrix'>::pop_back` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.AAMatrix'>::max_size` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.AAMatrix'>::clear` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.mean_field.AAMatrix'>::capacity` 
 - `[<class 'pyrosetta.rosetta.protocols.mean_field.jagged_array_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>]` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_utility_vector1_protocols_mean_field_AAProb_std_allocator_protocols_mean_field_AAProb_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.match.upstream.ProteinUpstreamBuilder'>::compatible` 
 - `[<class 'pyrosetta.rosetta.protocols.match.upstream.ProteinUpstreamBuilder'>, <class 'pyrosetta.rosetta.protocols.match.Hit'>, <class 'pyrosetta.rosetta.protocols.match.upstream.ScaffoldBuildPoint'>, <class 'pyrosetta.rosetta.protocols.match.upstream.UpstreamBuilder'>, <class 'pyrosetta.rosetta.protocols.match.Hit'>, <class 'pyrosetta.rosetta.protocols.match.upstream.ScaffoldBuildPoint'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.match.upstream.ProteinUpstreamBuilder'>, <class 'pyrosetta.rosetta.protocols.match.Hit'>, <class 'pyrosetta.rosetta.protocols.match.upstream.ScaffoldBuildPoint'>, <class 'pyrosetta.rosetta.protocols.match.upstream.ProteinUpstreamBuilder'>, <class 'pyrosetta.rosetta.protocols.match.Hit'>, <class 'pyrosetta.rosetta.protocols.match.upstream.ScaffoldBuildPoint'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.match.upstream.ProteinUpstreamBuilder'>::compatible` 
 - `[<class 'pyrosetta.rosetta.protocols.match.upstream.ProteinUpstreamBuilder'>, <class 'pyrosetta.rosetta.protocols.match.Hit'>, <class 'pyrosetta.rosetta.protocols.match.upstream.ScaffoldBuildPoint'>, <class 'pyrosetta.rosetta.protocols.match.upstream.UpstreamBuilder'>, <class 'pyrosetta.rosetta.protocols.match.Hit'>, <class 'pyrosetta.rosetta.protocols.match.upstream.ScaffoldBuildPoint'>, <class 'bool'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.match.upstream.ProteinUpstreamBuilder'>, <class 'pyrosetta.rosetta.protocols.match.Hit'>, <class 'pyrosetta.rosetta.protocols.match.upstream.ScaffoldBuildPoint'>, <class 'pyrosetta.rosetta.protocols.match.upstream.ProteinUpstreamBuilder'>, <class 'pyrosetta.rosetta.protocols.match.Hit'>, <class 'pyrosetta.rosetta.protocols.match.upstream.ScaffoldBuildPoint'>, <class 'bool'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.match.upstream.OriginalBackboneBuildPoint'>::compatible` 
 - `[<class 'pyrosetta.rosetta.protocols.match.upstream.OriginalBackboneBuildPoint'>, <class 'pyrosetta.rosetta.protocols.match.upstream.ScaffoldBuildPoint'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.match.upstream.OriginalBackboneBuildPoint'>, <class 'pyrosetta.rosetta.protocols.match.upstream.OriginalBackboneBuildPoint'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.match.upstream.OriginalBackboneBuildPoint'>::compatible` 
 - `[<class 'pyrosetta.rosetta.protocols.match.upstream.OriginalBackboneBuildPoint'>, <class 'pyrosetta.rosetta.protocols.match.upstream.ScaffoldBuildPoint'>, <class 'bool'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.match.upstream.OriginalBackboneBuildPoint'>, <class 'pyrosetta.rosetta.protocols.match.upstream.OriginalBackboneBuildPoint'>, <class 'bool'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.match.downstream.RigidLigandBuilder'>::compatible` 
 - `[<class 'pyrosetta.rosetta.protocols.match.downstream.RigidLigandBuilder'>, <class 'pyrosetta.rosetta.protocols.match.Hit'>, <class 'pyrosetta.rosetta.protocols.match.downstream.DownstreamBuilder'>, <class 'pyrosetta.rosetta.protocols.match.Hit'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.match.downstream.RigidLigandBuilder'>, <class 'pyrosetta.rosetta.protocols.match.Hit'>, <class 'pyrosetta.rosetta.protocols.match.downstream.RigidLigandBuilder'>, <class 'pyrosetta.rosetta.protocols.match.Hit'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.match.downstream.RigidLigandBuilder'>::compatible` 
 - `[<class 'pyrosetta.rosetta.protocols.match.downstream.RigidLigandBuilder'>, <class 'pyrosetta.rosetta.protocols.match.Hit'>, <class 'pyrosetta.rosetta.protocols.match.downstream.DownstreamBuilder'>, <class 'pyrosetta.rosetta.protocols.match.Hit'>, <class 'bool'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.match.downstream.RigidLigandBuilder'>, <class 'pyrosetta.rosetta.protocols.match.Hit'>, <class 'pyrosetta.rosetta.protocols.match.downstream.RigidLigandBuilder'>, <class 'pyrosetta.rosetta.protocols.match.Hit'>, <class 'bool'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.match.downstream.LigandConformerBuilder'>::compatible` 
 - `[<class 'pyrosetta.rosetta.protocols.match.downstream.LigandConformerBuilder'>, <class 'pyrosetta.rosetta.protocols.match.Hit'>, <class 'pyrosetta.rosetta.protocols.match.downstream.DownstreamBuilder'>, <class 'pyrosetta.rosetta.protocols.match.Hit'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.match.downstream.LigandConformerBuilder'>, <class 'pyrosetta.rosetta.protocols.match.Hit'>, <class 'pyrosetta.rosetta.protocols.match.downstream.LigandConformerBuilder'>, <class 'pyrosetta.rosetta.protocols.match.Hit'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.match.downstream.LigandConformerBuilder'>::compatible` 
 - `[<class 'pyrosetta.rosetta.protocols.match.downstream.LigandConformerBuilder'>, <class 'pyrosetta.rosetta.protocols.match.Hit'>, <class 'pyrosetta.rosetta.protocols.match.downstream.DownstreamBuilder'>, <class 'pyrosetta.rosetta.protocols.match.Hit'>, <class 'bool'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.match.downstream.LigandConformerBuilder'>, <class 'pyrosetta.rosetta.protocols.match.Hit'>, <class 'pyrosetta.rosetta.protocols.match.downstream.LigandConformerBuilder'>, <class 'pyrosetta.rosetta.protocols.match.Hit'>, <class 'bool'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.make_rot_lib.RotData'>` 
 - `[<class 'int'>, <class 'int'>, <class 'bool'>]` 
 - `[<class 'int'>, <class 'int'>, <class 'int'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.hotspot_hashing.SearchPatternTransform'>` 
 - `[<class 'pyrosetta.rosetta.protocols.hotspot_hashing.SearchPattern'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.hotspot_hashing.SearchPatternTransform'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.hotspot_hashing.SearchPatternExpansion'>` 
 - `[<class 'pyrosetta.rosetta.protocols.hotspot_hashing.SearchPattern'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.hotspot_hashing.SearchPatternExpansion'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.hbnet.HBNetScore'>` 
 - `[<class 'pyrosetta.rosetta.protocols.filters.Filter'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.hbnet.HBNetScore'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.generalized_kinematic_closure.GeneralizedKIC'>::add_filter_parameter` 
 - `[<class 'pyrosetta.rosetta.protocols.generalized_kinematic_closure.GeneralizedKIC'>, <class 'str'>, <class 'int'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.generalized_kinematic_closure.GeneralizedKIC'>, <class 'str'>, <class 'bool'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.generalized_kinematic_closure.GeneralizedKIC'>::add_filter_parameter` 
 - `[<class 'pyrosetta.rosetta.protocols.generalized_kinematic_closure.GeneralizedKIC'>, <class 'int'>, <class 'str'>, <class 'int'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.generalized_kinematic_closure.GeneralizedKIC'>, <class 'int'>, <class 'str'>, <class 'bool'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.generalized_kinematic_closure.filter.GeneralizedKICfilter'>::get_filter_param` 
 - `[<class 'pyrosetta.rosetta.protocols.generalized_kinematic_closure.filter.GeneralizedKICfilter'>, <class 'str'>, <class 'int'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.generalized_kinematic_closure.filter.GeneralizedKICfilter'>, <class 'str'>, <class 'bool'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.generalized_kinematic_closure.filter.GeneralizedKICfilter'>::add_filter_param` 
 - `[<class 'pyrosetta.rosetta.protocols.generalized_kinematic_closure.filter.GeneralizedKICfilter'>, <class 'str'>, <class 'int'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.generalized_kinematic_closure.filter.GeneralizedKICfilter'>, <class 'str'>, <class 'bool'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.frag_picker.BoundedCollector_protocols_frag_picker_CompareTotalScore_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.protocols.frag_picker.BoundedCollector_protocols_frag_picker_CompareTotalScore_t'>, <class 'pyrosetta.rosetta.protocols.frag_picker.BoundedCollector_protocols_frag_picker_CompareTotalScore_t'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.frag_picker.BoundedCollector_protocols_frag_picker_CompareTotalScore_t'>, <class 'pyrosetta.rosetta.protocols.frag_picker.CandidatesCollector'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.filters.ReplicateFilter'>` 
 - `[<class 'pyrosetta.rosetta.protocols.filters.Filter'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.filters.ReplicateFilter'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.evaluation.SingleValuePoseEvaluator_unsigned_long_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.protocols.evaluation.SingleValuePoseEvaluator_unsigned_long_t'>, <class 'pyrosetta.rosetta.protocols.evaluation.SingleValuePoseEvaluator_unsigned_long_t'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.evaluation.SingleValuePoseEvaluator_unsigned_long_t'>, <class 'pyrosetta.rosetta.protocols.evaluation.PoseEvaluator'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.evaluation.SingleValuePoseEvaluator_long_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.protocols.evaluation.SingleValuePoseEvaluator_long_t'>, <class 'pyrosetta.rosetta.protocols.evaluation.SingleValuePoseEvaluator_long_t'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.evaluation.SingleValuePoseEvaluator_long_t'>, <class 'pyrosetta.rosetta.protocols.evaluation.PoseEvaluator'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.evaluation.SingleValuePoseEvaluator_double_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.protocols.evaluation.SingleValuePoseEvaluator_double_t'>, <class 'pyrosetta.rosetta.protocols.evaluation.SingleValuePoseEvaluator_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.evaluation.SingleValuePoseEvaluator_double_t'>, <class 'pyrosetta.rosetta.protocols.evaluation.PoseEvaluator'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.environment.ProtectedConformation'>::assign` 
 - `[<class 'pyrosetta.rosetta.protocols.environment.ProtectedConformation'>, <class 'pyrosetta.rosetta.core.conformation.Conformation'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.environment.ProtectedConformation'>, <class 'pyrosetta.rosetta.protocols.environment.ProtectedConformation'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.docking.membrane.MPDockingMover'>` 
 - `[<class 'bool'>]` 
 - `[<class 'int'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.docking.membrane.MPDockingMover'>` 
 - `[<class 'bool'>, <class 'bool'>]` 
 - `[<class 'int'>, <class 'bool'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.denovo_design.components.VectorSelector_utility_vector1_std_shared_ptr_const_protocols_denovo_design_components_Segment_std_allocator_std_shared_ptr_const_protocols_denovo_design_components_Segment_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.protocols.denovo_design.components.VectorSelector_utility_vector1_std_shared_ptr_const_protocols_denovo_design_components_Segment_std_allocator_std_shared_ptr_const_protocols_denovo_design_components_Segment_t'>, <class 'pyrosetta.rosetta.protocols.denovo_design.components.VectorSelector_utility_vector1_std_shared_ptr_const_protocols_denovo_design_components_Segment_std_allocator_std_shared_ptr_const_protocols_denovo_design_components_Segment_t'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.denovo_design.components.VectorSelector_utility_vector1_std_shared_ptr_const_protocols_denovo_design_components_Segment_std_allocator_std_shared_ptr_const_protocols_denovo_design_components_Segment_t'>, <class 'pyrosetta.rosetta.utility.vector1_utility_vector1_std_shared_ptr_const_protocols_denovo_design_components_Segment_std_allocator_std_shared_ptr_const_protocols_denovo_design_components_Segment_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.denovo_design.components.EnumeratedVectorSelector_utility_vector1_std_shared_ptr_const_protocols_denovo_design_components_Segment_std_allocator_std_shared_ptr_const_protocols_denovo_design_components_Segment_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.protocols.denovo_design.components.EnumeratedVectorSelector_utility_vector1_std_shared_ptr_const_protocols_denovo_design_components_Segment_std_allocator_std_shared_ptr_const_protocols_denovo_design_components_Segment_t'>, <class 'pyrosetta.rosetta.protocols.denovo_design.components.VectorSelector_utility_vector1_std_shared_ptr_const_protocols_denovo_design_components_Segment_std_allocator_std_shared_ptr_const_protocols_denovo_design_components_Segment_t'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.denovo_design.components.EnumeratedVectorSelector_utility_vector1_std_shared_ptr_const_protocols_denovo_design_components_Segment_std_allocator_std_shared_ptr_const_protocols_denovo_design_components_Segment_t'>, <class 'pyrosetta.rosetta.utility.vector1_utility_vector1_std_shared_ptr_const_protocols_denovo_design_components_Segment_std_allocator_std_shared_ptr_const_protocols_denovo_design_components_Segment_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.denovo_design.components.EnumeratedVectorSelector_utility_vector1_std_shared_ptr_const_protocols_denovo_design_components_Segment_std_allocator_std_shared_ptr_const_protocols_denovo_design_components_Segment_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.protocols.denovo_design.components.EnumeratedVectorSelector_utility_vector1_std_shared_ptr_const_protocols_denovo_design_components_Segment_std_allocator_std_shared_ptr_const_protocols_denovo_design_components_Segment_t'>, <class 'pyrosetta.rosetta.protocols.denovo_design.components.EnumeratedVectorSelector_utility_vector1_std_shared_ptr_const_protocols_denovo_design_components_Segment_std_allocator_std_shared_ptr_const_protocols_denovo_design_components_Segment_t'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.denovo_design.components.EnumeratedVectorSelector_utility_vector1_std_shared_ptr_const_protocols_denovo_design_components_Segment_std_allocator_std_shared_ptr_const_protocols_denovo_design_components_Segment_t'>, <class 'pyrosetta.rosetta.utility.vector1_utility_vector1_std_shared_ptr_const_protocols_denovo_design_components_Segment_std_allocator_std_shared_ptr_const_protocols_denovo_design_components_Segment_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.denovo_design.components.EnumeratedVectorSelector_utility_vector1_std_shared_ptr_const_protocols_denovo_design_components_Segment_std_allocator_std_shared_ptr_const_protocols_denovo_design_components_Segment_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.protocols.denovo_design.components.EnumeratedVectorSelector_utility_vector1_std_shared_ptr_const_protocols_denovo_design_components_Segment_std_allocator_std_shared_ptr_const_protocols_denovo_design_components_Segment_t'>, <class 'pyrosetta.rosetta.protocols.denovo_design.components.EnumeratedVectorSelector_utility_vector1_std_shared_ptr_const_protocols_denovo_design_components_Segment_std_allocator_std_shared_ptr_const_protocols_denovo_design_components_Segment_t'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.denovo_design.components.EnumeratedVectorSelector_utility_vector1_std_shared_ptr_const_protocols_denovo_design_components_Segment_std_allocator_std_shared_ptr_const_protocols_denovo_design_components_Segment_t'>, <class 'pyrosetta.rosetta.protocols.denovo_design.components.VectorSelector_utility_vector1_std_shared_ptr_const_protocols_denovo_design_components_Segment_std_allocator_std_shared_ptr_const_protocols_denovo_design_components_Segment_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.constraints_additional.MaxSeqSepConstraintSet'>::assign` 
 - `[<class 'pyrosetta.rosetta.protocols.constraints_additional.MaxSeqSepConstraintSet'>, <class 'pyrosetta.rosetta.core.scoring.constraints.ConstraintSet'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.constraints_additional.MaxSeqSepConstraintSet'>, <class 'pyrosetta.rosetta.protocols.constraints_additional.MaxSeqSepConstraintSet'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.comparative_modeling.RecoverSideChainsMover'>` 
 - `[<class 'pyrosetta.rosetta.protocols.moves.Mover'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.comparative_modeling.RecoverSideChainsMover'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.comparative_modeling.IgnoreSubsetConstraintSet'>::assign` 
 - `[<class 'pyrosetta.rosetta.protocols.comparative_modeling.IgnoreSubsetConstraintSet'>, <class 'pyrosetta.rosetta.core.scoring.constraints.ConstraintSet'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.comparative_modeling.IgnoreSubsetConstraintSet'>, <class 'pyrosetta.rosetta.protocols.comparative_modeling.IgnoreSubsetConstraintSet'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.antibody.grafting.SCS_MultiTemplate'>` 
 - `[<class 'pyrosetta.rosetta.protocols.antibody.grafting.SCS_Base'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.antibody.grafting.SCS_MultiTemplate'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.antibody.grafting.SCS_BlastComparator'>::compare` 
 - `[<class 'pyrosetta.rosetta.protocols.antibody.grafting.SCS_BlastComparator'>, <class 'pyrosetta.rosetta.protocols.antibody.grafting.AntibodySequence'>, <class 'pyrosetta.rosetta.protocols.antibody.grafting.SCS_Result'>, <class 'pyrosetta.rosetta.protocols.antibody.grafting.SCS_Result'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.antibody.grafting.SCS_BlastComparator'>, <class 'pyrosetta.rosetta.protocols.antibody.grafting.AntibodySequence'>, <class 'pyrosetta.rosetta.protocols.antibody.grafting.SCS_BlastResult'>, <class 'pyrosetta.rosetta.protocols.antibody.grafting.SCS_BlastResult'>]`

CONFLICT `<class 'pyrosetta.rosetta.protocols.abinitio.KinematicTaskControl'>` 
 - `[<class 'pyrosetta.rosetta.protocols.abinitio.Protocol'>]` 
 - `[<class 'pyrosetta.rosetta.protocols.abinitio.KinematicTaskControl'>]`

CONFLICT `<class 'pyrosetta.rosetta.numeric.MathNTensor_double_6_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.numeric.MathNTensor_double_6_t'>, <class 'pyrosetta.rosetta.numeric.MathNTensor_double_6_t'>]` 
 - `[<class 'pyrosetta.rosetta.numeric.MathNTensor_double_6_t'>, <class 'pyrosetta.rosetta.numeric.MathNTensorBase_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.numeric.MathNTensor_double_5_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.numeric.MathNTensor_double_5_t'>, <class 'pyrosetta.rosetta.numeric.MathNTensor_double_5_t'>]` 
 - `[<class 'pyrosetta.rosetta.numeric.MathNTensor_double_5_t'>, <class 'pyrosetta.rosetta.numeric.MathNTensorBase_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.numeric.MathNTensor_double_4_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.numeric.MathNTensor_double_4_t'>, <class 'pyrosetta.rosetta.numeric.MathNTensor_double_4_t'>]` 
 - `[<class 'pyrosetta.rosetta.numeric.MathNTensor_double_4_t'>, <class 'pyrosetta.rosetta.numeric.MathNTensorBase_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.numeric.MathNTensor_double_3_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.numeric.MathNTensor_double_3_t'>, <class 'pyrosetta.rosetta.numeric.MathNTensor_double_3_t'>]` 
 - `[<class 'pyrosetta.rosetta.numeric.MathNTensor_double_3_t'>, <class 'pyrosetta.rosetta.numeric.MathNTensorBase_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.numeric.MathNTensor_double_2_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.numeric.MathNTensor_double_2_t'>, <class 'pyrosetta.rosetta.numeric.MathNTensor_double_2_t'>]` 
 - `[<class 'pyrosetta.rosetta.numeric.MathNTensor_double_2_t'>, <class 'pyrosetta.rosetta.numeric.MathNTensorBase_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.numeric.MathNTensor_double_1_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.numeric.MathNTensor_double_1_t'>, <class 'pyrosetta.rosetta.numeric.MathNTensor_double_1_t'>]` 
 - `[<class 'pyrosetta.rosetta.numeric.MathNTensor_double_1_t'>, <class 'pyrosetta.rosetta.numeric.MathNTensorBase_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.numeric.MathNTensor_bool_3_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.numeric.MathNTensor_bool_3_t'>, <class 'pyrosetta.rosetta.numeric.MathNTensor_bool_3_t'>]` 
 - `[<class 'pyrosetta.rosetta.numeric.MathNTensor_bool_3_t'>, <class 'pyrosetta.rosetta.numeric.MathNTensorBase_bool_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.numeric.interpolation.spline.PolycubicSpline_6_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.numeric.interpolation.spline.PolycubicSpline_6_t'>, <class 'pyrosetta.rosetta.numeric.interpolation.spline.PolycubicSpline_6_t'>]` 
 - `[<class 'pyrosetta.rosetta.numeric.interpolation.spline.PolycubicSpline_6_t'>, <class 'pyrosetta.rosetta.numeric.interpolation.spline.PolycubicSplineBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.numeric.interpolation.spline.PolycubicSpline_5_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.numeric.interpolation.spline.PolycubicSpline_5_t'>, <class 'pyrosetta.rosetta.numeric.interpolation.spline.PolycubicSpline_5_t'>]` 
 - `[<class 'pyrosetta.rosetta.numeric.interpolation.spline.PolycubicSpline_5_t'>, <class 'pyrosetta.rosetta.numeric.interpolation.spline.PolycubicSplineBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.numeric.interpolation.spline.PolycubicSpline_4_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.numeric.interpolation.spline.PolycubicSpline_4_t'>, <class 'pyrosetta.rosetta.numeric.interpolation.spline.PolycubicSpline_4_t'>]` 
 - `[<class 'pyrosetta.rosetta.numeric.interpolation.spline.PolycubicSpline_4_t'>, <class 'pyrosetta.rosetta.numeric.interpolation.spline.PolycubicSplineBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.numeric.interpolation.spline.PolycubicSpline_3_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.numeric.interpolation.spline.PolycubicSpline_3_t'>, <class 'pyrosetta.rosetta.numeric.interpolation.spline.PolycubicSpline_3_t'>]` 
 - `[<class 'pyrosetta.rosetta.numeric.interpolation.spline.PolycubicSpline_3_t'>, <class 'pyrosetta.rosetta.numeric.interpolation.spline.PolycubicSplineBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.numeric.interpolation.spline.PolycubicSpline_2_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.numeric.interpolation.spline.PolycubicSpline_2_t'>, <class 'pyrosetta.rosetta.numeric.interpolation.spline.PolycubicSpline_2_t'>]` 
 - `[<class 'pyrosetta.rosetta.numeric.interpolation.spline.PolycubicSpline_2_t'>, <class 'pyrosetta.rosetta.numeric.interpolation.spline.PolycubicSplineBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.numeric.interpolation.spline.PolycubicSpline_1_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.numeric.interpolation.spline.PolycubicSpline_1_t'>, <class 'pyrosetta.rosetta.numeric.interpolation.spline.PolycubicSpline_1_t'>]` 
 - `[<class 'pyrosetta.rosetta.numeric.interpolation.spline.PolycubicSpline_1_t'>, <class 'pyrosetta.rosetta.numeric.interpolation.spline.PolycubicSplineBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.numeric.expression_parser.UnaryExpression'>` 
 - `[<class 'pyrosetta.rosetta.numeric.expression_parser.Expression'>]` 
 - `[<class 'pyrosetta.rosetta.numeric.expression_parser.UnaryExpression'>]`

CONFLICT `<class 'pyrosetta.rosetta.numeric.expression_parser.SquarerootExpression'>` 
 - `[<class 'pyrosetta.rosetta.numeric.expression_parser.Expression'>]` 
 - `[<class 'pyrosetta.rosetta.numeric.expression_parser.SquarerootExpression'>]`

CONFLICT `<class 'pyrosetta.rosetta.numeric.expression_parser.NotExpression'>` 
 - `[<class 'pyrosetta.rosetta.numeric.expression_parser.Expression'>]` 
 - `[<class 'pyrosetta.rosetta.numeric.expression_parser.NotExpression'>]`

CONFLICT `<class 'pyrosetta.rosetta.numeric.expression_parser.AbsoluteValueExpression'>` 
 - `[<class 'pyrosetta.rosetta.numeric.expression_parser.Expression'>]` 
 - `[<class 'pyrosetta.rosetta.numeric.expression_parser.AbsoluteValueExpression'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.select.residue_selector.SymmetricalResidueSelector'>` 
 - `[<class 'pyrosetta.rosetta.core.select.residue_selector.ResidueSelector'>]` 
 - `[<class 'pyrosetta.rosetta.core.select.residue_selector.SymmetricalResidueSelector'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.select.residue_selector.ResidueVector'>` 
 - `[<class 'pyrosetta.rosetta.utility.vector1_unsigned_long'>]` 
 - `[<class 'pyrosetta.rosetta.core.select.residue_selector.ResidueVector'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.select.residue_selector.RandomGlycanFoliageSelector'>` 
 - `[<class 'pyrosetta.rosetta.core.select.residue_selector.ResidueSelector'>]` 
 - `[<class 'pyrosetta.rosetta.core.select.residue_selector.RandomGlycanFoliageSelector'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.select.residue_selector.NotResidueSelector'>` 
 - `[<class 'pyrosetta.rosetta.core.select.residue_selector.NotResidueSelector'>]` 
 - `[<class 'pyrosetta.rosetta.core.select.residue_selector.ResidueSelector'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.select.residue_selector.AndResidueSelector'>` 
 - `[<class 'pyrosetta.rosetta.core.select.residue_selector.AndResidueSelector'>]` 
 - `[<class 'pyrosetta.rosetta.core.select.residue_selector.ResidueSelector'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.select.jump_selector.NotJumpSelector'>` 
 - `[<class 'pyrosetta.rosetta.core.select.jump_selector.NotJumpSelector'>]` 
 - `[<class 'pyrosetta.rosetta.core.select.jump_selector.JumpSelector'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.select.jump_selector.AndJumpSelector'>` 
 - `[<class 'pyrosetta.rosetta.core.select.jump_selector.AndJumpSelector'>]` 
 - `[<class 'pyrosetta.rosetta.core.select.jump_selector.JumpSelector'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_mm_mmtrie_MMEnergyTableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_lkball_lkbtrie_LKBAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_hbonds_hbtrie_HBAtom_core_scoring_hbonds_hbtrie_HBCPData_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_hbonds_hbtrie_HBAtom_core_scoring_hbonds_hbtrie_HBCPData_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_hbonds_hbtrie_HBAtom_core_scoring_hbonds_hbtrie_HBCPData_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_hbonds_hbtrie_HBAtom_core_scoring_hbonds_hbtrie_HBCPData_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_hbonds_hbtrie_HBAtom_core_scoring_hbonds_hbtrie_HBCPData_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_hbonds_hbtrie_HBAtom_core_scoring_hbonds_hbtrie_HBCPData_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_hbonds_hbtrie_HBAtom_core_scoring_hbonds_hbtrie_HBCPData_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_hbonds_hbtrie_HBAtom_core_scoring_hbonds_hbtrie_HBCPData_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_hbonds_hbtrie_HBAtom_core_scoring_hbonds_hbtrie_HBCPData_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_hbonds_hbtrie_HBAtom_core_scoring_hbonds_hbtrie_HBCPData_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_hbonds_hbtrie_HBAtom_core_scoring_hbonds_hbtrie_HBCPData_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_hbonds_hbtrie_HBAtom_core_scoring_hbonds_hbtrie_HBCPData_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_hbonds_hbtrie_HBAtom_core_scoring_hbonds_hbtrie_HBCPData_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_hbonds_hbtrie_HBAtom_core_scoring_hbonds_hbtrie_HBCPData_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_hbonds_hbtrie_HBAtom_core_scoring_hbonds_hbtrie_HBCPData_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_hbonds_hbtrie_HBAtom_core_scoring_hbonds_hbtrie_HBCPData_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_hbonds_hbtrie_HBAtom_core_scoring_hbonds_hbtrie_HBCPData_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_hbonds_hbtrie_HBAtom_core_scoring_hbonds_hbtrie_HBCPData_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_hbonds_hbtrie_HBAtom_core_scoring_hbonds_hbtrie_HBCPData_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_hbonds_hbtrie_HBAtom_core_scoring_hbonds_hbtrie_HBCPData_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_hbonds_hbtrie_HBAtom_core_scoring_hbonds_hbtrie_HBCPData_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_hbonds_hbtrie_HBAtom_core_scoring_hbonds_hbtrie_HBCPData_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_hbonds_hbtrie_HBAtom_core_scoring_hbonds_hbtrie_HBCPData_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_hbonds_hbtrie_HBAtom_core_scoring_hbonds_hbtrie_HBCPData_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_hbonds_hbtrie_HBAtom_core_scoring_hbonds_hbtrie_HBCPData_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_hbonds_hbtrie_HBAtom_core_scoring_hbonds_hbtrie_HBCPData_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_hbonds_hbtrie_HBAtom_core_scoring_hbonds_hbtrie_HBCPData_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_hbonds_hbtrie_HBAtom_core_scoring_hbonds_hbtrie_HBCPData_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>::resolve_trie_vs_trie` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.ObjexxFCL.FArray2D_float_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairDataGeneric_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_3_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_2_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>::resolve_trie_vs_path` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_etable_etrie_EtableAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieCountPairBase'>, <class 'pyrosetta.rosetta.core.scoring.etable.TableLookupEvaluator'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.utility.vector1_float'>, <class 'pyrosetta.rosetta.core.scoring.trie.TrieVsTrieCachedDataContainerBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrie_core_scoring_elec_electrie_ElecAtom_core_scoring_etable_etrie_CountPairData_1_1_t'>, <class 'pyrosetta.rosetta.core.scoring.trie.RotamerTrieBase'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.symmetry.SymmetricEnergies'>` 
 - `[<class 'pyrosetta.rosetta.core.scoring.Energies'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.symmetry.SymmetricEnergies'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.symmetry.SymmetricEnergies'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.scoring.symmetry.SymmetricEnergies'>, <class 'pyrosetta.rosetta.core.scoring.Energies'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.symmetry.SymmetricEnergies'>, <class 'pyrosetta.rosetta.core.scoring.symmetry.SymmetricEnergies'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.solid_surface.SurfaceEnergies'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.scoring.solid_surface.SurfaceEnergies'>, <class 'pyrosetta.rosetta.core.scoring.Energies'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.solid_surface.SurfaceEnergies'>, <class 'pyrosetta.rosetta.core.scoring.solid_surface.SurfaceEnergies'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.MinScoreScoreFunction'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.scoring.MinScoreScoreFunction'>, <class 'pyrosetta.rosetta.core.scoring.ScoreFunction'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.MinScoreScoreFunction'>, <class 'pyrosetta.rosetta.core.scoring.MinScoreScoreFunction'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.hbonds.NPDHBondSet'>::show` 
 - `[<class 'pyrosetta.rosetta.core.scoring.hbonds.NPDHBondSet'>, <class 'pyrosetta.rosetta.core.pose.Pose'>, <class 'bool'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.hbonds.NPDHBondSet'>, <class 'pyrosetta.rosetta.core.pose.Pose'>, <class 'int'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.hbonds.HBondSet'>::show` 
 - `[<class 'pyrosetta.rosetta.core.scoring.hbonds.HBondSet'>, <class 'pyrosetta.rosetta.core.pose.Pose'>, <class 'bool'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.hbonds.HBondSet'>, <class 'pyrosetta.rosetta.core.pose.Pose'>, <class 'int'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.scoring.DockingScoreFunction'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.scoring.DockingScoreFunction'>, <class 'pyrosetta.rosetta.core.scoring.ScoreFunction'>]` 
 - `[<class 'pyrosetta.rosetta.core.scoring.DockingScoreFunction'>, <class 'pyrosetta.rosetta.core.scoring.DockingScoreFunction'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pose.PDBInfo'>::resize_atom_records` 
 - `[<class 'pyrosetta.rosetta.core.pose.PDBInfo'>, <class 'int'>, <class 'int'>]` 
 - `[<class 'pyrosetta.rosetta.core.pose.PDBInfo'>, <class 'int'>, <class 'bool'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.task.residue_selector.ClashBasedShellSelector'>` 
 - `[<class 'pyrosetta.rosetta.core.pack.task.residue_selector.ClashBasedShellSelector'>]` 
 - `[<class 'pyrosetta.rosetta.core.select.residue_selector.ResidueSelector'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_5_5_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_5_5_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_5_5_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_5_5_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_5_4_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_5_4_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_5_4_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_5_4_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_5_3_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_5_3_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_5_3_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_5_3_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_5_2_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_5_2_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_5_2_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_5_2_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_5_1_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_5_1_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_5_1_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_5_1_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_4_5_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_4_5_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_4_5_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_4_5_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_4_4_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_4_4_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_4_4_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_4_4_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_4_3_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_4_3_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_4_3_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_4_3_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_4_2_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_4_2_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_4_2_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_4_2_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_4_1_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_4_1_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_4_1_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_4_1_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_3_5_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_3_5_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_3_5_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_3_5_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_3_4_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_3_4_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_3_4_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_3_4_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_3_3_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_3_3_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_3_3_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_3_3_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_3_2_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_3_2_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_3_2_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_3_2_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_3_1_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_3_1_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_3_1_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_3_1_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_2_5_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_2_5_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_2_5_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_2_5_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_2_4_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_2_4_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_2_4_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_2_4_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_2_3_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_2_3_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_2_3_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_2_3_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_2_2_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_2_2_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_2_2_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_2_2_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_2_1_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_2_1_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_2_1_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_2_1_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_1_5_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_1_5_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_1_5_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_1_5_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_1_4_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_1_4_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_1_4_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_1_4_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_1_3_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_1_3_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_1_3_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_1_3_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_1_2_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_1_2_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_1_2_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_1_2_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_1_1_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_1_1_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_1_1_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_1_1_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_5_5_float_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_5_5_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_5_5_float_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_5_5_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_5_5_float_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_5_4_float_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_5_4_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_5_4_float_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_5_4_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_5_4_float_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_5_3_float_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_5_3_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_5_3_float_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_5_3_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_5_3_float_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_5_2_float_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_5_2_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_5_2_float_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_5_2_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_5_2_float_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_5_1_float_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_5_1_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_5_1_float_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_5_1_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_5_1_float_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_4_5_float_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_4_5_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_4_5_float_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_4_5_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_4_5_float_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_4_4_float_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_4_4_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_4_4_float_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_4_4_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_4_4_float_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_4_3_float_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_4_3_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_4_3_float_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_4_3_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_4_3_float_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_4_2_float_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_4_2_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_4_2_float_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_4_2_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_4_2_float_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_4_1_float_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_4_1_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_4_1_float_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_4_1_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_4_1_float_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_3_5_float_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_3_5_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_3_5_float_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_3_5_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_3_5_float_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_3_4_float_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_3_4_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_3_4_float_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_3_4_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_3_4_float_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_3_3_float_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_3_3_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_3_3_float_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_3_3_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_3_3_float_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_3_2_float_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_3_2_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_3_2_float_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_3_2_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_3_2_float_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_3_1_float_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_3_1_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_3_1_float_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_3_1_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_3_1_float_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_2_5_float_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_2_5_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_2_5_float_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_2_5_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_2_5_float_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_2_4_float_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_2_4_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_2_4_float_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_2_4_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_2_4_float_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_2_3_float_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_2_3_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_2_3_float_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_2_3_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_2_3_float_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_2_2_float_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_2_2_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_2_2_float_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_2_2_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_2_2_float_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_2_1_float_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_2_1_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_2_1_float_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_2_1_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_2_1_float_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_1_5_float_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_1_5_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_1_5_float_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_1_5_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_1_5_float_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_1_4_float_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_1_4_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_1_4_float_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_1_4_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_1_4_float_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_1_3_float_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_1_3_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_1_3_float_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_1_3_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_1_3_float_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_1_2_float_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_1_2_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_1_2_float_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_1_2_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_1_2_float_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_1_1_float_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_1_1_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_1_1_float_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.PackedDunbrackRotamer_1_1_float_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_1_1_float_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_5_5_double_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_5_5_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_5_5_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_5_5_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_5_5_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_5_4_double_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_5_4_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_5_4_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_5_4_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_5_4_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_5_3_double_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_5_3_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_5_3_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_5_3_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_5_3_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_5_2_double_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_5_2_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_5_2_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_5_2_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_5_2_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_5_1_double_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_5_1_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_5_1_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_5_1_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_5_1_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_4_5_double_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_4_5_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_4_5_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_4_5_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_4_5_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_4_4_double_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_4_4_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_4_4_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_4_4_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_4_4_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_4_3_double_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_4_3_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_4_3_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_4_3_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_4_3_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_4_2_double_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_4_2_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_4_2_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_4_2_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_4_2_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_4_1_double_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_4_1_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_4_1_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_4_1_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_4_1_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_3_5_double_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_3_5_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_3_5_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_3_5_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_3_5_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_3_4_double_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_3_4_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_3_4_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_3_4_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_3_4_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_3_3_double_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_3_3_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_3_3_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_3_3_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_3_3_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_3_2_double_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_3_2_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_3_2_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_3_2_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_3_2_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_3_1_double_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_3_1_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_3_1_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_3_1_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_3_1_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_2_5_double_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_2_5_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_2_5_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_2_5_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_2_5_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_2_4_double_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_2_4_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_2_4_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_2_4_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_2_4_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_2_3_double_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_2_3_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_2_3_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_2_3_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_2_3_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_2_2_double_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_2_2_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_2_2_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_2_2_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_2_2_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_2_1_double_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_2_1_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_2_1_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_2_1_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_2_1_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_1_5_double_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_1_5_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_1_5_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_1_5_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_1_5_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_1_4_double_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_1_4_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_1_4_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_1_4_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_1_4_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_1_3_double_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_1_3_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_1_3_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_1_3_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_1_3_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_1_2_double_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_1_2_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_1_2_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_1_2_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_1_2_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_1_1_double_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_1_1_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_1_1_double_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamer_1_1_double_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.DunbrackRotamerMeanSD_1_1_double_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_5_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_5_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_2_5_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_5_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_5_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_5_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_5_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_5_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_2_5_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_5_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_5_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_5_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_5_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_4_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_4_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_2_4_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_4_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_4_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_4_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_4_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_4_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_2_4_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_4_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_4_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_4_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_4_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_3_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_3_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_2_3_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_3_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_3_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_3_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_3_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_3_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_2_3_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_3_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_3_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_3_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_3_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_2_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_2_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_2_2_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_2_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_2_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_2_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_2_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_2_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_2_2_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_2_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_2_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_2_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_2_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_1_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_1_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_2_1_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_1_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_1_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_1_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_1_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_1_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_2_1_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_1_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_1_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_1_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_2_1_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_5_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_5_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_1_5_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_5_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_5_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_5_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_5_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_5_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_1_5_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_5_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_5_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_5_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_5_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_4_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_4_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_1_4_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_4_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_4_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_4_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_4_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_4_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_1_4_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_4_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_4_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_4_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_4_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_3_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_3_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_1_3_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_3_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_3_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_3_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_3_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_3_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_1_3_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_3_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_3_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_3_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_3_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_2_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_2_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_1_2_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_2_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_2_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_2_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_2_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_2_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_1_2_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_2_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_2_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_2_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_2_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_1_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_1_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_1_1_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_1_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_1_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_1_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_1_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_1_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamericData_1_1_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_1_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_1_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_1_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.pack.dunbrack.BBDepSemiRotamericData_1_1_t'>, <class 'pyrosetta.rosetta.core.pack.dunbrack.RotamerBuildingData'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.id.NamedAtomID_Map_bool_t'>` 
 - `[<class 'bool'>]` 
 - `[<class 'int'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.id.DOF_ID_Map_bool_t'>` 
 - `[<class 'bool'>]` 
 - `[<class 'int'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.id.AtomID_Map_bool_t'>` 
 - `[<class 'bool'>]` 
 - `[<class 'int'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.fragment.FragID_Iterator'>` 
 - `[<class 'pyrosetta.rosetta.core.fragment.ConstFrameIterator'>]` 
 - `[<class 'pyrosetta.rosetta.core.fragment.FrameIterator'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.fragment.FragCache_protocols_simple_moves_GunnTuple_t'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.fragment.FragCache_protocols_simple_moves_GunnTuple_t'>, <class 'pyrosetta.rosetta.core.fragment.FragCache_protocols_simple_moves_GunnTuple_t'>]` 
 - `[<class 'pyrosetta.rosetta.core.fragment.FragCache_protocols_simple_moves_GunnTuple_t'>, <class 'pyrosetta.rosetta.core.fragment.CacheWrapper_protocols_simple_moves_GunnTuple_core_fragment_MapCacheUnit_protocols_simple_moves_GunnTuple_t'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.fragment.ConstantLengthFragSet'>` 
 - `[<class 'pyrosetta.rosetta.core.fragment.FragSet'>]` 
 - `[<class 'pyrosetta.rosetta.core.fragment.ConstantLengthFragSet'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.conformation.symmetry.SymmetricConformation'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.conformation.symmetry.SymmetricConformation'>, <class 'pyrosetta.rosetta.core.conformation.Conformation'>]` 
 - `[<class 'pyrosetta.rosetta.core.conformation.symmetry.SymmetricConformation'>, <class 'pyrosetta.rosetta.core.conformation.symmetry.SymmetricConformation'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.conformation.symmetry.MirrorSymmetricConformation'>::assign` 
 - `[<class 'pyrosetta.rosetta.core.conformation.symmetry.MirrorSymmetricConformation'>, <class 'pyrosetta.rosetta.core.conformation.Conformation'>]` 
 - `[<class 'pyrosetta.rosetta.core.conformation.symmetry.MirrorSymmetricConformation'>, <class 'pyrosetta.rosetta.core.conformation.symmetry.MirrorSymmetricConformation'>]`

CONFLICT `<class 'pyrosetta.rosetta.core.chemical.PoseResidueTypeSet'>` 
 - `[<class 'pyrosetta.rosetta.core.chemical.ResidueTypeSet'>]` 
 - `[<class 'pyrosetta.rosetta.core.chemical.PoseResidueTypeSet'>]`

CONFLICT `<built-in method write_binary of PyCapsule object at 0x2aaadfa77ea0>` 
 - `[<class 'bool'>, <class 'pyrosetta.rosetta.core.io.serialization.BUFFER'>]` 
 - `[<class 'int'>, <class 'pyrosetta.rosetta.core.io.serialization.BUFFER'>]`

CONFLICT `<built-in method read_binary of PyCapsule object at 0x2aaadfa77ed0>` 
 - `[<class 'bool'>, <class 'pyrosetta.rosetta.core.io.serialization.BUFFER'>]` 
 - `[<class 'int'>, <class 'pyrosetta.rosetta.core.io.serialization.BUFFER'>]`

CONFLICT `<built-in method insert_pose_into_pose of PyCapsule object at 0x2aaae0537cc0>` 
 - `[<class 'pyrosetta.rosetta.core.pose.Pose'>, <class 'pyrosetta.rosetta.core.pose.Pose'>, <class 'int'>, <class 'int'>]` 
 - `[<class 'pyrosetta.rosetta.core.pose.Pose'>, <class 'pyrosetta.rosetta.core.pose.Pose'>, <class 'int'>, <class 'bool'>]`

CONFLICT `<built-in method create_rotamer_string of PyCapsule object at 0x2aade85d51a0>` 
 - `[<class 'pyrosetta.rosetta.core.pose.Pose'>, <class 'int'>, <class 'bool'>]` 
 - `[<class 'pyrosetta.rosetta.core.pose.Pose'>, <class 'int'>, <class 'int'>]`
