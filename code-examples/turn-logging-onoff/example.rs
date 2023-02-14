let mut session = Session::new();

if session.is_enabled() {
    println!("Logging is already on.");
} else {
    session.set_enabled(true);
}