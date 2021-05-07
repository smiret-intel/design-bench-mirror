from design_bench.registration import registry, register, make, spec
from design_bench.task import Task


register('GFP-GP-v0',
         'design_bench.datasets.discrete:GFPDataset',
         'design_bench.oracles.sklearn:GaussianProcessOracle',
         dataset_kwargs=dict(max_samples=5000,
                             max_percentile=60,
                             min_percentile=50),
         oracle_kwargs=dict(noise_std=0.0))

register(
    'GFP-v1',
    'design_bench.tasks.gfp_v1:GFPV1Task',
    kwargs=dict(split_percentile=20,
                ys_noise=0.0))

register(
    'MoleculeActivity-v0',
    'design_bench.tasks.molecule_activity_v0:MoleculeActivityV0Task',
    kwargs=dict(target_assay=600885,
                split_percentile=80,
                ys_noise=0.0))

register(
    'TfBind8-v0',
    'design_bench.tasks.tfbind8_v0:TfBind8V0Task',
    kwargs=dict(split_percentile=20,
                transcription_factor='SIX6_REF_R1',
                ys_noise=0.0))

register(
    'TfBind10-v0',
    'design_bench.tasks.tfbind10_v0:TfBind10V0Task',
    kwargs=dict(split_percentile=20,
                transcription_factor='pho4',
                ys_noise=0.0))

register(
    'UTRExpression-v0',
    'design_bench.tasks.utr_expression_v0:UTRExpressionV0Task',
    kwargs=dict(split_percentile=20,
                ys_noise=0.0))

register(
    'Superconductor-v0',
    'design_bench.tasks.superconductor:SuperconductorTask',
    kwargs=dict(split_percentile=80,
                ys_noise=0.0))

try:

    import mujoco_py  # test that MuJoCo is installed
    import morphing_agents  # test that Morphing-Agents is installed
    from morphing_agents.mujoco.ant.env \
        import MorphingAntEnv
    from morphing_agents.mujoco.ant.elements \
        import LEG as ANT_LEG
    from morphing_agents.mujoco.ant.elements \
        import LEG_LOWER_BOUND as ANT_LEG_LOWER_BOUND
    from morphing_agents.mujoco.ant.elements \
        import LEG_UPPER_BOUND as ANT_LEG_UPPER_BOUND
    from morphing_agents.mujoco.dkitty.env \
        import MorphingDKittyEnv
    from morphing_agents.mujoco.dkitty.elements \
        import LEG as DKITTY_LEG
    from morphing_agents.mujoco.dkitty.elements \
        import LEG_LOWER_BOUND as DKITTY_LEG_LOWER_BOUND
    from morphing_agents.mujoco.dkitty.elements \
        import LEG_UPPER_BOUND as DKITTY_LEG_UPPER_BOUND

    register(
        'HopperController-v0',
        'design_bench.tasks.controller_v0:ControllerV0Task',
        kwargs=dict(
            obs_dim=11,
            action_dim=3,
            hidden_dim=64,
            env_name='Hopper-v2',
            x_file='hopper_controller_v0_X.npy',
            y_file='hopper_controller_v0_y.npy',
            split_percentile=100,
            ys_noise=0.0))

    register(
        'HopperController-v1',
        'design_bench.tasks.controller_v1:ControllerV1Task',
        kwargs=dict(
            obs_dim=11,
            action_dim=3,
            hidden_dim=256,
            env_name='Hopper-v2',
            x_file='hopper_controller_v1_X.npy',
            y_file='hopper_controller_v1_y.npy',
            split_percentile=80,
            ys_noise=0.0))

    register(
        'AntMorphology-v0',
        'design_bench.tasks.morphology_v0:MorphologyV0Task',
        kwargs=dict(
            env_class=MorphingAntEnv,
            elements=4,
            env_element=ANT_LEG,
            env_element_lb=ANT_LEG_LOWER_BOUND,
            env_element_ub=ANT_LEG_UPPER_BOUND,
            oracle_weights='ant_oracle.pkl',
            x_file='ant_morphology_X.npy',
            y_file='ant_morphology_y.npy',
            split_percentile=20,
            num_rollouts=1,
            rollout_horizon=100,
            num_parallel=1,
            ys_noise=0.0))

    register(
        'DKittyMorphology-v0',
        'design_bench.tasks.morphology_v0:MorphologyV0Task',
        kwargs=dict(
            env_class=MorphingDKittyEnv,
            elements=4,
            env_element=DKITTY_LEG,
            env_element_lb=DKITTY_LEG_LOWER_BOUND,
            env_element_ub=DKITTY_LEG_UPPER_BOUND,
            oracle_weights='dkitty_oracle.pkl',
            x_file='dkitty_morphology_X.npy',
            y_file='dkitty_morphology_y.npy',
            split_percentile=40,
            num_rollouts=1,
            rollout_horizon=100,
            num_parallel=1,
            ys_noise=0.0))

except ImportError as e:

    print('Skipping registration of: '
          'HopperController-v0, '
          'HopperController-v1, '
          'AntMorphology-v0, '
          'DKittyMorphology-v0')
